# lib/models/game.py

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import sessionmaker, relationship
from models.__init__ import Base, engine

class Game(Base):

    __tablename__ = 'games'

    game_id = Column(Integer, primary_key = True)
    home = Column(String, nullable = False)
    away = Column(String, nullable = False)
    date = Column(Date, nullable = False)
    time = Column(Time, nullable = False)
    location = Column(String, nullable =False)

    __table_args__ = (
        UniqueConstraint('date', 'time', 'location', name='unique_game_details'),
    )