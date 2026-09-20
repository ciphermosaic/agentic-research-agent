from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY, MODEL_NAME
from app.agent.prompts import (
    PLANNER_PROMPT,
    ANALYST_PROMPT,
    FACT_CHECK_PROMPT,
    REPORT_PROMPT
)
from app.tools.web_search import search_web
from app.rag.vectorstore import search_documents
from langgraph.types import interrupt

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)


def planner_node(state):

    query = state["query"]

    prompt = f"""
    {PLANNER_PROMPT}

    Research question:
    {query}
    """

    response = llm.invoke(prompt)

    plan = [
        line.strip()
        for line in response.content.split("\n")
        if line.strip()
    ]

    return {
        "research_plan": plan
    }


def research_node(state):

    plan = state["research_plan"]

    search_results = []
    documents = []

    for question in plan:

        web_results = search_web(question)

        search_results.extend(web_results)

        try:
            rag_results = search_documents(question)

            for doc in rag_results:
                documents.append({
                    "content": doc.page_content,
                    "metadata": doc.metadata
                })

        except Exception:
            pass

    return {
        "search_results": search_results,
        "documents": documents
    }


def analysis_node(state):

    web_text = "\n\n".join(
        [
            f"Title: {item.get('title', '')}\n"
            f"Content: {item.get('content', '')}\n"
            f"URL: {item.get('url', '')}"
            for item in state["search_results"]
        ]
    )

    rag_text = "\n\n".join(
        [
            f"Document: {item['metadata']}\n"
            f"Content: {item['content']}"
            for item in state["documents"]
        ]
    )

    prompt = f"""
{ANALYST_PROMPT}

USER QUESTION:
{state["query"]}

WEB RESEARCH:
{web_text}

INTERNAL DOCUMENTS:
{rag_text}
"""

    response = llm.invoke(prompt)

    return {
        "analysis": response.content
    }


def fact_check_node(state):

    prompt = f"""
{FACT_CHECK_PROMPT}

QUESTION:
{state["query"]}

ANALYSIS:
{state["analysis"]}
"""

    response = llm.invoke(prompt)

    content = response.content

    needs_more = "MORE_RESEARCH" in content

    return {
        "fact_check": content,
        "needs_more_research": needs_more,
        "iteration": state["iteration"] + 1
    }


def report_node(state):

    sources = "\n".join(
        [
            f"- {item.get('title', 'Unknown')}: {item.get('url', '')}"
            for item in state["search_results"]
        ]
    )

    prompt = f"""
{REPORT_PROMPT}

QUESTION:
{state["query"]}

RESEARCH PLAN:
{state["research_plan"]}

ANALYSIS:
{state["analysis"]}

FACT CHECK:
{state["fact_check"]}

SOURCES:
{sources}
"""

    response = llm.invoke(prompt)

    return {
        "report": response.content
    }


def human_review_node(state):

    review = interrupt(
        {
            "type": "research_review",

            "message": (
                "The research phase is complete. "
                "Please review the findings before "
                "the final report is generated."
            ),

            "query": state["query"],

            "analysis": state["analysis"],

            "fact_check": state["fact_check"]
        }
    )

    approved = review.get(
        "approved",
        False
    )

    feedback = review.get(
        "feedback",
        ""
    )

    return {
        "human_approved": approved,
        "human_feedback": feedback
    }

print("done")