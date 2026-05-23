import re


def extract_sql_query(text: str):

    # Remove markdown fences
    text = re.sub(
        r"```sql",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"```",
        "",
        text
    )

    # Find first SELECT query
    match = re.search(
        r"(SELECT[\s\S]+?;)",
        text,
        flags=re.IGNORECASE
    )

    if not match:
        raise ValueError(
            "No valid SQL query found."
        )

    return match.group(1).strip()