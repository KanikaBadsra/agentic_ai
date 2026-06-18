from sqlalchemy import inspect
from app.database.connection import engine
inspector = inspect(engine)
for table in inspector.get_table_names():
    print('TABLE', table)
    for col in inspector.get_columns(table):
        print(' ', col['name'], col['type'])

