import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()

database = os.getenv('POSTGRES_DB', 'postgres')
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('POSTGRES_HOST', 'postgres')
port = os.getenv('POSTGRES_PORT', 5432)

DATABASE = PostgresqlDatabase(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
)

DEFAULT_PAGES_COUNT = 20
