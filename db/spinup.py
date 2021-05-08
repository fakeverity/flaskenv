from sqlalchemy       import create_engine, MetaData
from sqlalchemy.orm   import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
from getpass          import getpass
from os               import environ
from dotenv           import load_dotenv

conf = load_dotenv()

# Obtain database info
# -----------------------------------
DB_NAME     = environ.get("DB_NAME")
ALCHEMY_URL = environ.get("ALCHEMY_URL")

print( "\nDatabase: ", DB_NAME, "\n\n" )

# Configure ALCHEMY properties 
# -----------------------------------
Engine   = create_engine(ALCHEMY_URL, echo=True)
Session  = sessionmaker()
Metadata = MetaData(bind=Engine)
Base     = declarative_base(metadata=Metadata)

Engine.connect()
Session.configure(bind=Engine)


