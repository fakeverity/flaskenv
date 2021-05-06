from sqlalchemy import(
      Column
    , Integer
    , String
    , DateTime
    , MetaData
    , create_engine as mkengine
)
from sqlalchemy.orm import declarativ_base 
from os import environ

# Initialize alchemy utils
# ------------------------
Base   = declarative_base()
engine = mkengine(environ.get("ALCHEMY_URL"))


# Define record & table models
# ----------------------------
class User(Base):
    __tablename__ = 'users'

    id        = Column(Integer, primary_key=True)
    name      = Column(String)
    full_name = Column(String)
    username  = Column(String)
    created   = Column(DateTime, nullable=False, server_default=func.sysdate()) 

