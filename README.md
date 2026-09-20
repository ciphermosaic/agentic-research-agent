🤖 Agentic Research Agent

An end-to-end Agentic AI Research Agent built with LangGraph, LangChain, MCP, memory, RAG, and human-in-the-loop workflows.

The goal of this project is to build an AI agent that can research a topic, gather relevant information, reason over the collected context, and eventually generate a structured research report.

---

✨ Features

Current

- 🤖 Agentic workflow using LangGraph
- 🧠 Stateful agent architecture
- 🔎 Web research capabilities
- 🛠️ Tool-based agent execution
- 📚 RAG pipeline
- 💾 Persistent memory
- 🔌 MCP integration
- 👤 Human-in-the-loop architecture
- ⚙️ Environment-based configuration
- 🐍 Python-based backend

Planned

- 📊 Advanced research synthesis
- 📝 Automated report generation
- 🔍 Improved source verification
- 🧠 Advanced long-term memory
- 👤 More human approval checkpoints
- 🐳 Complete Docker deployment

---

🏗️ Architecture

                         User
                          │
                          ▼
                   Research Query
                          │
                          ▼
                  ┌───────────────┐
                  │   LangGraph   │
                  │     Agent     │
                  └───────┬───────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          Web Search     RAG         MCP Tools
             │            │            │
             └────────────┼────────────┘
                          ▼
                       Memory
                          │
                          ▼
                  Research Context
                          │
                          ▼
                  Future: Report
                     Generation

---

📂 Project Structure

agentic-research-agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api.py
│   └── config.py
│
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── graph.py
│   │   ├── state.py
│   │   ├── nodes.py
│   │   └── tools.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── cleaning.py
│   │   ├── metadata.py
│   │   ├── vectorstore.py
│   │   └── retriever.py
│   │
│   ├── memory/
│   │   ├── __init__.py
│   │   └── memory.py
│   │
│   ├── mcp/
│   │   ├── __init__.py
│   │   └── client.py
│   │
│   └── prompts.py
│
├── data/
│   └── *.pdf
│
├── tests/
│
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

---

🧠 How It Works

The agent receives a research question and processes it through a stateful workflow.

1. User Query

The user provides a research topic.

Research the impact of AI agents on software development.

2. Agent Workflow

LangGraph manages the workflow and maintains the state of the research process.

3. Information Retrieval

The agent can use external tools and the project's RAG pipeline to retrieve relevant information.

4. RAG

Local PDF documents can be processed and indexed for retrieval.

PDF Documents
      │
      ▼
Document Loading
      │
      ▼
Text Cleaning
      │
      ▼
Metadata
      │
      ▼
Embeddings
      │
      ▼
Vector Store
      │
      ▼
Retriever

The project also supports hybrid retrieval using semantic and keyword-based retrieval.

5. Memory

The agent maintains information across interactions so that previous research context can be reused.

6. MCP

Model Context Protocol is used to provide a standardized way for the agent to interact with external tools and resources.

7. Human-in-the-Loop

The architecture allows human approval or intervention at important points in the workflow.

---

🛠️ Tech Stack

Technology| Purpose
Python| Core programming language
LangGraph| Agent workflow and state management
LangChain| Agent and LLM tooling
MCP| Tool and context integration
ChromaDB| Vector database
Hugging Face| Embeddings
BM25| Keyword retrieval
FastAPI| Backend API
PyPDF| PDF processing
Docker| Containerization

---

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/ciphermosaic/agentic-research-agent.git
cd agentic-research-agent

2. Create a Virtual Environment

python -m venv venv

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Create Environment Variables

Create a ".env" file in the project root:

OPENAI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key

Add any additional API keys required by the tools you configure.

5. Add Research Documents

Place PDF documents inside:

data/

Example:

data/
├── paper1.pdf
├── paper2.pdf
└── paper3.pdf

6. Run the Project

python -m app.main

If using the FastAPI server:

uvicorn app.api:app --reload

---

🔎 Example Research Query

What are the latest developments in Agentic AI?

The agent can use its available tools and knowledge sources to gather information and process the research context.

---

🧩 Development Phases

Phase 1, Core Agent

Completed

- Project architecture
- LangGraph workflow
- Agent state
- Agent nodes
- Tool integration
- Basic research workflow
- Configuration management

---

Phase 2, RAG + Memory + MCP + Human-in-the-Loop

Completed

- RAG pipeline
- PDF ingestion
- Document processing
- Vector storage
- Hybrid retrieval
- Persistent memory
- MCP integration
- Human-in-the-loop architecture

---

Phase 3, Observability + Advanced Agent

Planned

- LangSmith tracing
- Advanced observability
- Improved agent reasoning
- Better source verification
- More sophisticated memory
- Research planning
- Automated report generation
- Human approval checkpoints
- Agent evaluation
- Production deployment

---

📌 Roadmap

Phase 1
Core Agent
   │
   ▼
Phase 2
RAG + Memory + MCP + HITL
   │
   ▼
Phase 3
Observability + Advanced Agent
   │
   ▼
Phase 4
Report Generation + Evaluation
   │
   ▼
Phase 5
Production Deployment

---

🎯 Project Goals

This project demonstrates practical Agentic AI engineering, including:

- Stateful AI agents
- Multi-step workflows
- Tool calling
- Retrieval-Augmented Generation
- Long-term memory
- MCP
- Human-in-the-loop systems
- Agent observability
- Production-oriented architecture

The long-term goal is to build a research assistant capable of conducting research and producing structured reports with human oversight.

---

🔮 Future Improvements

Multi-agent research architecture
Parallel web research
Source credibility evaluation
Automatic citation generation
Research planning and task decomposition
Streaming responses
Agent evaluation
LangSmith monitoring
Authentication
Web interface
Cloud deployment
Scheduled research tasks
---

👨‍💻 Author

Abu Bakar

AI/ML Engineering Student

GitHub: "https://github.com/ciphermosaic"

Hugging Face: "https://huggingface.co/ciphermosaic"

