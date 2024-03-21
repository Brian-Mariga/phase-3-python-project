from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import sessionmaker, relationship
from models.__init__ import Base, engine

class Teams(Base):

    __tablename__ = 'teams'

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String, nullable = False, unique= True)
