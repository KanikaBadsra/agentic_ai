from app.agents.supervisor_agent import (
    supervisor_agent
)

from app.graphs.nodes.sql_node import sql_node

from app.graphs.nodes.rag_node import rag_node

from app.agents.analytics_agent import (
    analytics_agent
)


def multi_agent_node(state):

    question = state["question"]

    selected_agents = supervisor_agent(
        question
    )

    state["selected_agents"] = (
        selected_agents
    )

    if "sql_agent" in selected_agents:

        sql_result = sql_node(state)

        state.update(sql_result)

    if "rag_agent" in selected_agents:

        rag_result = rag_node(state)

        state.update(rag_result)

    if "analytics_agent" in selected_agents:

        analytics_result = analytics_agent(
            state
        )

        state.update(analytics_result)

    return state