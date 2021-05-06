from sqlalchemy import(
      Column
    , Integer
    , String
    , DateTime
    , MetaData
    , func
)
from sqlalchemy.orm import declarative_base 
from os import environ
from db.spinup import ALCDB

# Initialize alchemy utils
# ------------------------
dbInstance = ALCDB()
Base = dbInstance.Base
Base.metadata.create_all(Engine)

# ----------------------------
class User(Base):
    __tablename__ = 'users'

    id        = Column(Integer, primary_key=True)
    name      = Column(String)
    full_name = Column(String)
    username  = Column(String)
    created   = Column(DateTime, nullable=False, server_default=func.sysdate()) 

