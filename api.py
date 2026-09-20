from fastapi import FastAPI
from pydantic import BaseModel

from app.main import (
    run_research
)


app = FastAPI(
    title="AI Research & Report Agent",
    description=(
        "Agentic AI research system "
        "using LangGraph, RAG, MCP and memory."
    ),
    version="1.0.0"
)


class ResearchRequest(
    BaseModel
):

    query: str


class ResearchResponse(
    BaseModel
):

    query: str

    report: str


@app.get("/")
def root():

    return {
        "application": (
            "AI Research & Report Agent"
        ),
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post(
    "/research",
    response_model=ResearchResponse
)
def research(
    request: ResearchRequest
):

    result = run_research(
        request.query
    )

    return ResearchResponse(
        query=request.query,
        report=result["report"]
    )