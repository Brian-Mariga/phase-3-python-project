# lib/models/player_statistics.py

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
    player = relationship("Player", back_populates="statistics")
    game = relationship("Game", back_populates="player_statistics")

    __table_arg__ = (UniqueConstraint('player_id', 'game_id', name='unique_player_game_stats'),)

    def add_statistics():
        pass

    def get_player_statistics():
        pass

    def get_game_statistics():
        pass

    def update_statistic():
        pass

    def delete_statistic():
        pass