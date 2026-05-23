import pandas as pd
from sqlalchemy import text

from app.database.connection import engine


def execute_query(query: str):

    with engine.connect() as connection:
        result = connection.execute(text(query))

        rows = result.fetchall()

        columns = result.keys()

        df = pd.DataFrame(rows, columns=columns)

        return df.to_dict(orient="records")