from app.agents.sql_agent import generate_sql
from app.database.query_executor import execute_query
from app.utils.sql_extractor import extract_sql_query
from app.utils.sql_validator import validate_sql
from app.observability.logger import logger
from app.observability.timer import track_time

@track_time("SQL Node")
def sql_node(state):

    question = state["question"]

    sql_query = generate_sql(question)
    #sql_query = clean_sql_query(sql_query)
    sql_query = extract_sql_query(sql_query)
    validate_sql(sql_query)

    result = execute_query(sql_query)

    logger.info(f"SQL Query executed: {sql_query}")
    logger.info(f"Query result: {result}")

    return {
        "sql_query": sql_query,
        "result": result
    }