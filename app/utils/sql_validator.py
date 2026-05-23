FORBIDDEN_KEYWORDS = [
    "DROP",
    "DELETE",
    "UPDATE",
    "ALTER",
    "TRUNCATE",
    "INSERT",
    "CREATE"
]


def validate_sql(query: str):

    upper_query = query.upper()

    for keyword in FORBIDDEN_KEYWORDS:

        if keyword in upper_query:
            raise ValueError(
                f"Forbidden SQL operation detected: {keyword}"
            )

    return True