from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# Historical reference: original supervisor-based routing implementation.
# This was replaced by a multi-agent node that handles routing internally.
# from app.graphs.nodes.report_node import report_node
# from app.graphs.nodes.sql_node import sql_node
# from app.graphs.nodes.rag_node import rag_node
# from app.graphs.nodes.hybrid_node import hybrid_node
# from app.graphs.nodes.router_node import router_node
# from app.graphs.routing import decide_route
from app.graphs.nodes.summarizer_node import summarizer_node
from app.graphs.nodes.multi_agent_node import (
    multi_agent_node
)

class GraphState(TypedDict):
    question: str
    route: str
    sql_query: str
    session_id: str
    conversation_history: str
    result: list
    documents: list
    final_answer: str

builder = StateGraph(GraphState)

# Historical note: multi-agent node now handles routing internally,
# replacing the previous supervisor/router based implementation.
# builder.add_node("router", router_node)
# builder.add_node("sql_agent", sql_node)
# builder.add_node("rag_agent", rag_node)
# builder.add_node("hybrid_agent", hybrid_agent)
# builder.add_node("report_agent", report_node)
# builder.add_node("summarizer", summarizer_node)
#
# builder.add_edge("router", "rag_agent")
# builder.add_edge("rag_agent", "sql_agent")
# builder.add_edge("sql_agent", "summarizer")
# builder.add_edge("summarizer", END)
#
# builder.set_entry_point("router")
# builder.add_conditional_edges(
#     "router",
#     decide_route,
#     {
#         "sql": "sql_agent",
#         "rag": "rag_agent",
#         "both": "hybrid_agent"
#     }
# )
#
# Previous simpler routing configuration (deprecated):
# builder.add_edge("sql_agent", "summarizer")
# builder.add_edge("rag_agent", "summarizer")
# builder.add_edge("summarizer", "report_agent")
# builder.add_edge("summarizer", END)


# ADD NODES
builder.add_node(
    "multi_agent",
    multi_agent_node
)

builder.add_node(
    "summarizer",
    summarizer_node
)

# GRAPH FLOW
builder.add_edge(
    START,
    "multi_agent"
)

builder.add_edge(
    "multi_agent",
    "summarizer"
)

builder.add_edge(
    "summarizer",
    END
)
graph = builder.compile()