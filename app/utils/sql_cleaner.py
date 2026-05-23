import re


def clean_sql_query(query: str):

    query = query.strip()

    # Remove markdown sql fences
    query = re.sub(r"```sql", "", query, flags=re.IGNORECASE)

    query = re.sub(r"```", "", query)

    return query.strip()