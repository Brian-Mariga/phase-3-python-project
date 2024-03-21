from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import sessionmaker, relationship
from models.__init__ import Base, engine

class Player(Base):

    __tablename__ = 'players'

    player_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    jersey_number = Column(Integer, nullable=False, unique=True)
    contact_details = Column(String, nullable=False, unique=True)
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    team = relationship("Teams", back_populates="players")


