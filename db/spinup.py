from sqlalchemy       import create_engine
from sqlalchemy_utils import database_exists, create_database
from getpass          import getpass
from os               import environ


def init_db():
    dburl = environ.get("ALCHEMIC_URL")
    engine = create_engine(dburl, echo=True)

    if not database_exists(engine.url):
        create_database(engine.url)
    else:
        engine.connect()
