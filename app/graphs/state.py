from typing import TypedDict, List


class GraphState(TypedDict):

    question: str

    session_id: str

    selected_agents: str

    sql_query: str

    sql_result: str

    rag_result: str

    analytics_result: str

    final_answer: str

    execution_trace: List[str]

    execution_time: dict

    active_agent: str
    confidence_score: float

    risk_level: str

    requires_human_review: bool
    guardrail_status: str