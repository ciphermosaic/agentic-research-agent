from langchain_tavily import TavilySearch
from app.config import TAVILY_API_KEY
from langchain_core.tools import tool

search_tool = TavilySearch(
    max_results=5,
    topic="general",
    tavily_api_key=TAVILY_API_KEY
)

@tool
def search_web(query:str) -> str:
    """Search the web for information"""
    result = search_tool.invoke({"query": query})

    if isinstance(result, dict):
        return result.get("results", [])

    return result
