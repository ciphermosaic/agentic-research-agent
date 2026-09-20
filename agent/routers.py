def research_router(state):

    if (
        state["needs_more_research"]
        and state["iteration"] < 2
    ):
        return "research"

    return "human_review"


def human_review_router(state):

    if state["human_approved"]:
        return "report"

    return "research"