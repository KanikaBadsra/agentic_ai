NexusIQ/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── chat.py
│   │   │   ├── auth.py
│   │   │   ├── health.py
│   │   │   └── admin.py
│   │   │
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── logging.py
│   │   └── constants.py
│   │
│   ├── graphs/
│   │   ├── main_graph.py
│   │   ├── state.py
│   │   ├── nodes/
│   │   │   ├── intent_node.py
│   │   │   ├── sql_node.py
│   │   │   ├── rag_node.py
│   │   │   ├── mcp_node.py
│   │   │   ├── summary_node.py
│   │   │   └── validator_node.py
│   │   │
│   │   └── edges/
│   │       └── routing.py
│   │
│   ├── agents/
│   │   ├── sql_agent.py
│   │   ├── rag_agent.py
│   │   ├── analyst_agent.py
│   │   └── action_agent.py
│   │
│   ├── rag/
│   │   ├── embeddings/
│   │   ├── loaders/
│   │   ├── chunking/
│   │   ├── vectorstore/
│   │   ├── retriever.py
│   │   └── ingestion.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── schema_cache.py
│   │   └── query_executor.py
│   │
│   ├── mcp/
│   │   ├── clients/
│   │   │   ├── jira_client.py
│   │   │   ├── slack_client.py
│   │   │   └── github_client.py
│   │   │
│   │   └── tool_registry.py
│   │
│   ├── services/
│   │   ├── llm_service.py
│   │   ├── prompt_service.py
│   │   ├── memory_service.py
│   │   └── auth_service.py
│   │
│   ├── prompts/
│   │   ├── sql/
│   │   ├── rag/
│   │   ├── summarizer/
│   │   └── classifier/
│   │
│   ├── memory/
│   │   ├── session_memory.py
│   │   └── conversation_store.py
│   │
│   ├── observability/
│   │   ├── tracing.py
│   │   ├── metrics.py
│   │   └── monitoring.py
│   │
│   ├── utils/
│   │   ├── helpers.py
│   │   ├── sql_sanitizer.py
│   │   └── token_counter.py
│   │
│   └── main.py
│
├── frontend/
│   ├── streamlit_app.py
│   └── components/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample_docs/
│
├── notebooks/
│   ├── rag_experiments.ipynb
│   └── sql_testing.ipynb
│
├── tests/
│   ├── test_api/
│   ├── test_graphs/
│   ├── test_agents/
│   ├── test_rag/
│   └── test_database/
│
├── scripts/
│   ├── ingest_docs.py
│   ├── init_db.py
│   └── seed_data.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── .env
├── requirements.txt
├── README.md
├── .gitignore
└── pyproject.toml




#############################################################

Most Important Folders Explained
/graphs

This is your LangGraph orchestration layer.

Interviewers will look here first.

Contains:

state definitions
workflow nodes
routing logic
/agents

Specialized AI agents.

Example:

SQL Agent
RAG Agent
Analyst Agent

Shows proper separation of concerns.

/rag

Complete RAG pipeline.

Includes:

chunking
embeddings
retrieval
ingestion

This demonstrates strong AI engineering skills.

/mcp

MCP integrations.

This is a major differentiator in interviews.

Even one integration:

Jira
Slack
GitHub

looks impressive.

/database

Production-grade DB handling.

Should include:

safe query execution
schema caching
repositories
/observability

VERY important.

Most candidates skip this.

Include:

logging
tracing
metrics

Shows production maturity.