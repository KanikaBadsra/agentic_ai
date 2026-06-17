#from app.services.llm_service import llm
from app.observability.logger import logger
from app.observability.timer import track_time
from app.memory.conversation_memory import (
    get_conversation_history
)
from app.llm.models import SUMMARY_LLM
from app.utils.tracing import add_trace
from app.utils.timer import (
    start_timer,
    end_timer
)
from app.services.confidence_service import (
    calculate_confidence,
    determine_risk,
    requires_human_review
)
llm = SUMMARY_LLM
@track_time("Summarizer Node")
def summarizer_node(state):
    timer = start_timer()

    state["active_agent"] = "summarizer_agent"

    add_trace(
        state,
        "Summarizer Node Started"
    )
    question = state["question"]

    sql_result = state.get("result", [])

    documents = state.get("documents", [])
    history = get_conversation_history(
    state["session_id"]
)
    prompt = f"""
You are an enterprise business analyst.
Conversation History:
{history}

User Question:
{question}

SQL Results:
{sql_result}

Retrieved Documents:
{documents}

Generate a concise business insight.
"""

    response = llm.invoke(prompt)
    
    logger.info(
    f"Final answer: {response.content}"
)
    duration = end_timer(timer)

    add_trace(
        state,
        f"Summarizer Node Completed ({duration}s)"
    )

    confidence = calculate_confidence(
    state
)

    risk_level = determine_risk(
        confidence
    )

    requires_review = requires_human_review(
    confidence
)

    return {
        "final_answer": response.content,

        "confidence_score": confidence,

        "risk_level": risk_level,

        "requires_human_review": requires_review
    }