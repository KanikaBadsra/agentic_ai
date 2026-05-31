from app.rag.retriever import retrieve_documents
from app.observability.logger import logger
from app.observability.timer import track_time
from app.utils.tracing import add_trace
from app.utils.timer import (
    start_timer,
    end_timer
)

@track_time("RAG Node")
def rag_node(state):
    timer = start_timer()

    state["active_agent"] = "rag_agent"

    add_trace(
        state,
        "RAG Agent Started"
    )
    question = state["question"]

    documents = retrieve_documents(question)
    logger.info(
        f"Retrieved documents: {documents}"
    )
    duration = end_timer(timer)

    add_trace(
        state,
        f"RAG Agent Completed ({duration}s)"
    )
    return {
        "documents": documents
    }