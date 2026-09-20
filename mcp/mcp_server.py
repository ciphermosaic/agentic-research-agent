from mcp.server.fastmcp import FastMCP

from langchain_tavily import TavilySearch

from app.config import TAVILY_API_KEY


mcp = FastMCP(
    "Research Tools"
)


search = TavilySearch(
    max_results=5,
    topic="general",
    tavily_api_key=TAVILY_API_KEY
)


@mcp.tool()
def web_search(
    query: str
) -> str:
    """
    Search the web for research information.
    """

    try:

        result = search.invoke(
            {
                "query": query
            }
        )

        return str(result)

    except Exception as e:

        return f"Search error: {e}"


@mcp.tool()
def calculate(
    expression: str
) -> str:
    """
    Calculate a mathematical expression.
    """

    try:

        result = eval(
            expression,
            {
                "__builtins__": {}
            },
            {}
        )

        return str(result)

    except Exception as e:

        return f"Calculation error: {e}"


@mcp.tool()
def get_research_instructions() -> str:
    """
    Return instructions describing how the
    research tools should be used.
    """

    return """
    Available research tools:

    1. web_search
       Search the internet for current information.

    2. calculate
       Perform mathematical calculations.

    Use web_search when current or external
    information is required.
    """


if __name__ == "__main__":

    mcp.run(
        transport="stdio"
    )