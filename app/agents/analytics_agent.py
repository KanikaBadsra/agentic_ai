# from langchain_ollama import ChatOllama
# llm = ChatOllama(
#     model="llama3"
# )
from app.llm.models import ANALYTICS_LLM
llm = ANALYTICS_LLM

def analytics_agent(state):

    sql_result = state.get(
        "sql_result",
        ""
    )

    rag_result = state.get(
        "rag_result",
        ""
    )

    prompt = f"""
You are a business analytics AI.

Analyze:
- trends
- risks
- decline causes
- opportunities

SQL DATA:
{sql_result}


DOCUMENT CONTEXT:
{rag_result}
"""

    response = llm.invoke(prompt)

    return {
        "analytics_result": response.content
    }