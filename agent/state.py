from typing import (
    TypedDict,
    List,
    Dict,
    Any
)


class ResearchState(TypedDict):

    query: str

    research_plan: List[str]

    search_results: List[Dict[str, Any]]

    documents: List[Dict[str, Any]]

    analysis: str

    fact_check: str

    report: str

    iteration: int

    needs_more_research: bool

    previous_research: List[
        Dict[str, Any]
    ]

    human_approved: bool

    human_feedback: str