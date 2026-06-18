from app.agents.sql_agent import generate_sql
from app.database.query_executor import execute_query
from app.utils.sql_extractor import extract_sql_query
from app.utils.sql_validator import validate_sql
from app.observability.logger import logger
from app.observability.timer import track_time
from app.utils.tracing import add_trace
from app.utils.timer import (
    start_timer,
    end_timer
)

@track_time("SQL Node")
def sql_node(state):
    timer = start_timer()

    state["active_agent"] = "sql_agent"

    add_trace(
        state,
        "SQL Agent Started"
)

    question = state["question"]

    sql_query = generate_sql(question)
    #sql_query = clean_sql_query(sql_query)
    sql_query = extract_sql_query(sql_query)
    is_safe = validate_sql(sql_query)
    if not is_safe:
        logger.warning(
            f"Generated SQL query failed validation: {sql_query}"
        )
        return {
            "sql_query": sql_query,
            "sql_result": [],
            "guardrail_status": "BLOCKED",
            "validation_error": "Generated SQL query failed safety validation."
        }
    
    try:
        result = execute_query(sql_query)
        logger.info(f"SQL Query executed: {sql_query}")
        logger.info(f"Query result: {result}")
        guardrail_status = "PASSED"
    except Exception as error:
        logger.error(f"SQL execution failed: {error}")        
        guardrail_status = "BLOCKED"
        sql_query = sql_query
        state["sql_error"] = str(error)

    duration = end_timer(timer)

    add_trace(
        state,
        f"SQL Agent Completed ({duration}s)"
    )
    return {
        "sql_query": sql_query,
        "sql_result": result,
        "guardrail_status": guardrail_status
    }