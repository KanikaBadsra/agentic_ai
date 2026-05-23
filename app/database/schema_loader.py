from sqlalchemy import inspect
from app.database.connection import engine

def get_database_schema():

    inspector = inspect(engine)

    schema_text = ""

    tables = inspector.get_table_names()

    for table in tables:

        schema_text += f"\nTable: {table}\n"

        columns = inspector.get_columns(table)

        for column in columns:

            schema_text += (
                f"- {column['name']} "
                f"({column['type']})\n"
            )

    return schema_text