import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase, SqliteDatabase

load_dotenv()

database = os.getenv('database')

DATABASE = SqliteDatabase(database)

DEFAULT_PAGES_COUNT = 20
