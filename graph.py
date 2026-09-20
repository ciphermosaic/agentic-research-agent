from nodes import (
    planner_node,
    research_node,
    analysis_node,
    fact_check_node,
    report_node
)
from state import ResearchState
from langgraph.graph import StateGraph, START, END

def research_router(state):

    if (
        state["needs_more_research"]
        and state["iteration"] < 2
    ):
        return "research"

    return "report"

def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("planner", planner_node)

    graph.add_node(
        "research",
        research_node
    )

    graph.add_node(
        "analysis",
        analysis_node
    )

    graph.add_node(
        "fact_check",
        fact_check_node
    )

    graph.add_node(
        "report",
        report_node
    )

    graph.set_entry_point("planner")

    graph.add_edge(
        "planner",
        "research"
    )

    graph.add_edge(
        "research",
        "analysis"
    )

    graph.add_edge(
        "analysis",
        "fact_check"
    )

    graph.add_conditional_edges(
        "fact_check",
        research_router,
        {
            "research": "research",
            "report": "report"
        }
    )

    graph.add_edge(
        "report",
        END
    )

    return graph.compile()

research_graph = build_graph()