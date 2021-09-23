import os

PG_HOST = os.environ["PG_HOST"]

SQLALCHEMY_DATABASE_URI = f"postgresql://user:user@localhost:5432/task-db"
