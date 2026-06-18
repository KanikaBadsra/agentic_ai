# from app.services.llm_service import llm


# SYSTEM_PROMPT = """
# You are an expert PostgreSQL assistant.

# Convert user questions into PostgreSQL queries.

# Rules:
# - Return ONLY SQL
# - No markdown
# - No explanations
# - Use existing tables only

# Tables:

# customers(
#     customer_id,
#     customer_name,
#     email,
#     country,
#     signup_date
# )

# products(
#     product_id,
#     product_name,
#     category,
#     price
# )

# regions(
#     region_id,
#     region_name
# )

# sales(
#     sale_id,
#     customer_id,
#     product_id,
#     region_id,
#     quantity,
#     total_amount,
#     sale_date
# )
# """


# def generate_sql(question: str):

#     response = llm.invoke(
#         f"{SYSTEM_PROMPT}\n\nUser Question: {question}"
#     )

#     return response.content.strip()


#from app.services.llm_service import llm
from app.database.schema_loader import get_database_schema
from app.llm.models import SQL_LLM
llm = SQL_LLM

def generate_sql(question: str):

    schema = get_database_schema()

    prompt = f"""
You are an expert PostgreSQL assistant.

Generate ONLY valid PostgreSQL SELECT queries.

Rules:
- Only SELECT queries
- No markdown
- NO explanations
- Use ONLY existing tables/columns
- Do not reference columns that are not present in the schema.
- If filtering by region, use sales.region_id and join to regions.region_id.
- The regions table contains region_name.

Database Schema:

{schema}

User Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip()