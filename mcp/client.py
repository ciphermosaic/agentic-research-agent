
from langchain_mcp_adapters.client import MultiServerMCPClient

from app.config import (
    MCP_SERVER_COMMAND
)


async def get_mcp_client():

    client = MultiServerMCPClient(
        {
            "research_tools": {
                "command": MCP_SERVER_COMMAND,
                "args": [
                    "mcp_server/server.py"
                ],
                "transport": "stdio"
            }
        }
    )

    return client


async def get_mcp_tools():

    client = await get_mcp_client()

    tools = await client.get_tools()

    return tools

















# from mcp import ClientSession
# from mcp.client.stdio import stdio_client
# from mcp import StdioServerParameters


# server_parameters = StdioServerParameters(
#     command="python",
#     args=[
#         "mcp_server/server.py"
#     ]
# )


# async def list_mcp_tools():

#     async with stdio_client(
#         server_parameters
#     ) as (
#         read,
#         write
#     ):

#         async with ClientSession(
#             read,
#             write
#         ) as session:

#             await session.initialize()

#             tools = await session.list_tools()

#             return tools.tools


# async def call_mcp_tool(
#     tool_name: str,
#     arguments: dict
# ):

#     async with stdio_client(
#         server_parameters
#     ) as (
#         read,
#         write
#     ):

#         async with ClientSession(
#             read,
#             write
#         ) as session:

#             await session.initialize()

#             result = await session.call_tool(
#                 tool_name,
#                 arguments
#             )

#             return result           