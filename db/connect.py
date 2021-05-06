from sqlalchemy import create_engine
from os import getenv


DB_HOST = getenv('DATABASE_HOST')
DB_NAME = getenv('DATABASE_NAME')
DB_USER = getenv('DATABASE_USER')
DB_PASS = getenv('DATABASE_PASS')
DB_CONN = f"postgresql+pg8000://{ DB_USER }:{ DB_PASS }@{ DB_HOST }/{ DB_NAME }"

if DB_HOST and DB_NAME and DB_USER and DB_PASS:
    engine = create_engine()
else: print(DB_CONN)
