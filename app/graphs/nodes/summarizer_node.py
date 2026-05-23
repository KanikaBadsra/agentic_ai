#from app.services.llm_service import llm
from app.observability.logger import logger
from app.observability.timer import track_time
from app.memory.conversation_memory import (
    get_conversation_history
)
from app.llm.models import SUMMARY_LLM

llm = SUMMARY_LLM
@track_time("Summarizer Node")
def summarizer_node(state):

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
    return {
        "final_answer": response.content
    }