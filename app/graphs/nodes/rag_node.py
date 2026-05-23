from app.rag.retriever import retrieve_documents
from app.observability.logger import logger
from app.observability.timer import track_time

@track_time("RAG Node")
def rag_node(state):

    question = state["question"]

    documents = retrieve_documents(question)
    logger.info(
        f"Retrieved documents: {documents}"
    )
    return {
        "documents": documents
    }