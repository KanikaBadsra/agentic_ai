from sqlalchemy import text

from app.database.connection import engine


def save_message(
    session_id,
    role,
    message
):

    query = text("""
        INSERT INTO conversations
        (session_id, role, message)
        VALUES
        (:session_id, :role, :message)
    """)

    with engine.begin() as connection:

        connection.execute(
            query,
            {
                "session_id": session_id,
                "role": role,
                "message": message
            }
        )

def get_conversation_history(
    session_id,
    limit=5
):

    query = text("""
        SELECT role, message
        FROM conversations
        WHERE session_id = :session_id
        ORDER BY created_at DESC
        LIMIT :limit
    """)

    with engine.connect() as connection:

        result = connection.execute(
            query,
            {
                "session_id": session_id,
                "limit": limit
            }
        )

        rows = result.fetchall()

    history = []

    for row in reversed(rows):

        history.append(
            f"{row.role}: {row.message}"
        )

    return "\n".join(history)