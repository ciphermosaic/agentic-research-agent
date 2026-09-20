from app.agent.graph import (
    research_graph
)

from app.memory.database import (
    initialize_database
)


def run_research(
    query: str
):

    initialize_database()

    initial_state = {

        "query": query,

        "research_plan": [],

        "search_results": [],

        "documents": [],

        "analysis": "",

        "fact_check": "",

        "report": "",

        "iteration": 0,

        "needs_more_research": False,

        "previous_research": []
    }

    result = research_graph.invoke(
        initial_state
    )

    return result


def main():

    print(
        "\n=============================="
    )

    print(
        "   AI RESEARCH AGENT"
    )

    print(
        "==============================\n"
    )

    query = input(
        "Enter your research question:\n> "
    )

    if not query.strip():

        print(
            "Please enter a research question."
        )

        return

    print(
        "\nAgent is researching..."
    )

    result = run_research(
        query
    )

    print(
        "\n=============================="
    )

    print(
        "FINAL REPORT"
    )

    print(
        "==============================\n"
    )

    print(
        result["report"]
    )


if __name__ == "__main__":

    main()