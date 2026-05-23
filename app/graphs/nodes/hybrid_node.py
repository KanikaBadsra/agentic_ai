from app.graphs.nodes.report_node import report_node
from app.graphs.nodes.rag_node import rag_node
from app.graphs.nodes.sql_node import sql_node
from app.graphs.nodes.summarizer_node import summarizer_node
from app.observability.timer import track_time

@track_time("Hybrid Node")
def hybrid_node(state):

    # STEP 1 → RAG Retrieval
    rag_result = rag_node(state)

    state.update(rag_result)

    # STEP 2 → SQL Retrieval
    sql_result = sql_node(state)

    state.update(sql_result)

    # STEP 3 → Final Summary
    summary_result = summarizer_node(state)

    state.update(summary_result)

     # STEP 4 → REPORT GENERATION
    report_result = report_node(state)

    state.update(report_result)

    return state