from sqlalchemy import(
      Column
    , Integer
    , String
    , DateTime
    , MetaData
    , Table
    , Enum
)
from   sqlalchemy.orm import declarative_base 
from   os             import environ
import datetime
import db.spinup
import enum


# ALCHEMY CONFIGURATION
# ---------------------------------
Base = db.spinup.Base
Engine = db.spinup.Engine

# USER ROLES
# ---------------------------------
class UserRoles(enum.Enum):
    admin   = 1
    stuff   = 2
    garbage = 3

# USER MODEL
# ---------------------------------
class User(Base):
    __tablename__ = 'users'

    id        = Column(Integer, primary_key=True)
    full_name = Column(String)
    username  = Column(String, nullable=False)
    password  = Column(String, nullable=True)
    created   = Column(DateTime, nullable=False, default=datetime.datetime.utcnow()) 
    role      = Column(Integer, nullable=False, default=UserRoles.garbage)

Base.metadata.create_all(Engine)

