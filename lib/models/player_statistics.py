from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import sessionmaker, relationship
from models.__init__ import Base, engine

class PlayerStatistics(Base):
    __tablename__ = 'player_statistics'

    stat_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.player_id'))
    game_id = Column(Integer, ForeignKey('games.game_id'))
    points_scored = Column(Integer)
    rebounds = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    player = relationship("Players", back_populates="statistics")
    game = relationship("Games", back_populates="player_statistics")