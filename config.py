import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MODEL_NAME = "openai/gpt-oss-120b"
VECTORSTORE_PATH = "./vectorstore"
DOCUMENT_PATH = "./data/documents" 

MCP_SERVER_COMMAND = "python"

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MEMORY_DB_PATH = BASE_DIR / "data" / "memory.db"