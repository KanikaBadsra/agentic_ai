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
from app.services.approval_service import create_approval
llm = SUMMARY_LLM
approval_id = None


@track_time("Summarizer Node")
def summarizer_node(state):
    timer = start_timer()

    state["active_agent"] = "summarizer_agent"

    add_trace(
        state,
        "Summarizer Node Started"
    )
    question = state["question"]

    sql_result = state.get("sql_result", state.get("result", []))
    documents = state.get("documents", [])

    try:
        history = get_conversation_history(state["session_id"])
    except Exception as error:
        logger.warning(f"Conversation history unavailable: {error}")
        history = []

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

    try:
        response = llm.invoke(prompt)
        answer = getattr(response, "content", str(response))
    except Exception as error:
        logger.error(f"Summarizer LLM call failed: {error}")
        answer = "I couldn't generate a final answer right now."

    logger.info(f"Final answer: {answer}")
    duration = end_timer(timer)

    add_trace(
        state,
        f"Summarizer Node Completed ({duration}s)"
    )

    confidence = calculate_confidence(state)
    risk_level = determine_risk(confidence)
    requires_review = requires_human_review(confidence)
    approval_id = None

    if requires_review:
        approval_id = create_approval(state)

    guardrail_status = state.get("guardrail_status", "PASSED" if answer else "BLOCKED")

    return {
        "final_answer": answer,
        "confidence_score": confidence,
        "risk_level": risk_level,
        "requires_human_review": requires_review,
        "approval_id": approval_id,
        "guardrail_status": guardrail_status
    }