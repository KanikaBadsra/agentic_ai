from app.observability.logger import logger
from app.observability.timer import track_time

@track_time("Router Node")
def router_node(state):

    question = state["question"].lower()

    sql_keywords = [
        "sales",
        "revenue",
        "customer",
        "product",
        "region",
        "database",
        "top selling"
    ]

    rag_keywords = [
        "report",
        "document",
        "policy",
        "summary",
        "pdf",
        "notes"
    ]

    sql_match = any(
        word in question
        for word in sql_keywords
    )

    rag_match = any(
        word in question
        for word in rag_keywords
    )

    if sql_match and rag_match:
        route = "both"

    elif sql_match:
        route = "sql"

    elif rag_match:
        route = "rag"

    else:
        route = "rag"

    logger.info(f"Routing decision made: {route}")

    return {
        "route": route
    }
