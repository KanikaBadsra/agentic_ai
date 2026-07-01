import re


def extract_sql_query(text: str):
    if not text or not str(text).strip():
        raise ValueError("No valid SQL query found.")

    text = str(text).strip()

    # Remove markdown fences
    text = re.sub(r"```(?:sql)?", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    # Find the first SELECT query, even if it has no trailing semicolon
    match = re.search(
        r"\bSELECT\b[\s\S]+?(?:;|$)",
        text,
        flags=re.IGNORECASE
    )

    if not match:
        raise ValueError("No valid SQL query found.")

    sql = match.group(0).strip()
    if sql.endswith(";"):
        sql = sql[:-1].rstrip()

    return sql