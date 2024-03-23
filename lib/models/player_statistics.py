# lib/models/player_statistics.py

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import sessionmaker, relationship
from models.__init__ import Base, session

class PlayerStatistics(Base):
    __tablename__ = 'player_statistics'

    stat_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.player_id'), nullable = False)
    game_id = Column(Integer, ForeignKey('games.game_id'), nullable = False)
    points_scored = Column(Integer)
    rebounds = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    player = relationship("Player", back_populates="statistics")
    game = relationship("Game", back_populates="player_statistics")

    __table_arg__ = (UniqueConstraint('player_id', 'game_id', name='unique_player_game_stats'),)

    def add_statistics(player_id, game_id, points_scored = 0, rebounds = 0, assists = 0, steals = 0, blocks = 0):
        if not player_id or not game_id:
            print("Player ID and Game id are required: ")
        else:
            new_statistic = PlayerStatistics(player_id = player_id,game_id = game_id,points_scored = points_scored,rebounds = rebounds,assists = assists,steals = steals,blocks = blocks)

            try:
                session.add(new_statistic)
                session.commit()
                print("Statistics successfully added")
            except Exception as exc:
                session.rollback()
                print(f'Error: {exc}')

    def get_all_statistics():
        return session.query(PlayerStatistics).all()
    
    def get_statistic_by_id(stat_id):
        return session.query(PlayerStatistics).filter(PlayerStatistics.stat_id == stat_id).first()
    
    def get_player_statistics(player_id):
        return session.query(PlayerStatistics).filter(PlayerStatistics.player_id == player_id).all()

    def get_game_statistics(game_id):
        return session.query(PlayerStatistics).filter(PlayerStatistics.game_id == game_id).all()
    
    @classmethod
    def get_stat_with_highest(cls, attribute):
        valid_attributes = ['points_scored', 'rebounds', 'assists, steals', 'blocks']

        if attribute not in valid_attributes:
            raise ValueError("Invalid attribute. Please provide one of: 'points_scored', 'rebounds', 'assists', 'steals', 'blocks'")
        return session.query(cls).order_by(getattr(cls,attribute).desc()).first()

    @classmethod
    def get_stat_with_lowest(cls, attribute):
        valid_attributes = ['points_scored', 'rebounds', 'assists, steals', 'blocks']

        if attribute not in valid_attributes:
            raise ValueError("Invalid attribute. Please provide one of: 'points_scored', 'rebounds', 'assists', 'steals', 'blocks'")
        return session.query(cls).order_by(getattr(cls,attribute).asc()).first()
        
    def update_statistic(stat_id):
        if stat := PlayerStatistics.get_statistic_by_id(stat_id):
            try:
                new_player_id = input("Enter the new Player ID: ")
                new_game_id = input("Enter the new Game ID: ")
                new_points_scored = input("Enter the new number of Points Scored: ")
                new_rebounds = input("Enter the new number of rebounds: ")
                new_assists = input("Enter the new number of assists: ")
                new_steals = input("Enter the new number of steals: ")
                new_blocks = input("Enter the new number of blocks: ")

                if new_player_id:
                    stat.player_id = new_player_id
                if new_game_id:
                    stat.game_id = new_game_id
                if new_points_scored:
                    stat.points_scored = new_points_scored
                if new_rebounds:
                    stat.rebounds = new_rebounds
                if new_assists:
                    stat.assists = new_assists
                if new_steals:
                    stat.steals = new_steals
                if new_blocks:
                    stat.blocks = new_blocks

                session.commit()
                print("Stats succesfully updated:\n", )

            except Exception as exc:
                session.rollback()
                print(f"Error updating statistic's details: {exc}")

    def delete_statistic(stat_id):
        if stat := PlayerStatistics.get_statistic_by_id(stat_id):
            try:
                session.delete(stat)
                session.commit()
                print("Statistic successfully deleted:\n",{stat})
            except Exception as exc:
                session.rollback()
                print("Error deleting statistic")
        else:
            print(f"Stats if ID {stat_id} not found")