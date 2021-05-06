from sqlalchemy       import create_engine
from sqlalchemy.orm   import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
from getpass          import getpass
from os               import environ


class ALCDB:
   
    __instance = None
    def __init__(self):
        if not ALCDB.__instance:
            ALCDB.DB_NAME=environ.get("DB_NAME")
            dburl = environ.get("ALCHEMY_URL")
            print (ALCDB.DB_NAME)

            self.__instance.Engine = create_engine(self.dburl, echo=True)
            self.__instance.Engine.connect()

            self.__instance.Session=sessionmaker()
            self.__instance.Session.configure(bind=engine)

            self.__instance.Base = declarative_base()

            if not engine:
                print("Successfully initialized db connection")

            if not database_exists(self().Engine.url):
                print("Target database: %db, doesn't exist, creating...", self.DB_NAME)
                create_database(self().Engine.url)
            else:
                engine.connect()
                print("** Database connection established successfully!: ", self.DB_NAME, "\n\n")
        else:
            self.getInstance()


    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = ALCDB()
        return cls.__instance

    
