# from langchain_ollama import ChatOllama

# llm = ChatOllama(
#     model="tinyllama"
# )

from app.llm.models import ROUTER_LLM

llm = ROUTER_LLM

def supervisor_agent(question):

    prompt = f"""
You are an AI supervisor.

Decide which agents should handle
the user request.

AVAILABLE AGENTS:
- sql_agent
- rag_agent
- analytics_agent

RULES:
- sales/data questions → sql_agent
- document/knowledge questions → rag_agent
- trend/insight/risk questions → analytics_agent
- multiple agents allowed

Return ONLY comma separated agents.


Question:
{question}
"""

    response = llm.invoke(prompt)

    agents = response.content.strip()

    return agents