# lib/models/statistics.py

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time, func
from sqlalchemy.orm import sessionmaker, relationship
from models.__init__ import Base, session

class Statistics(Base):
    __tablename__ = 'statistics'

    stat_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.player_id'), nullable = False)
    game_id = Column(Integer, ForeignKey('games.game_id'), nullable = False)
    points_scored = Column(Integer)
    rebounds = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    player = relationship("Player", back_populates="statistics")
    game = relationship("Game", back_populates="statistics")

    __table_arg__ = (UniqueConstraint('player_id', 'game_id', name='unique_player_game_stats'),)

    def add_statistics(player_id, game_id, points_scored = 0, rebounds = 0, assists = 0, steals = 0, blocks = 0):
        if not player_id or not game_id:
            print("Player ID and Game id are required: ")
        else:
            new_statistic = Statistics(player_id = player_id,game_id = game_id,points_scored = points_scored,rebounds = rebounds,assists = assists,steals = steals,blocks = blocks)

            try:
                session.add(new_statistic)
                session.commit()
                print("Statistics successfully added")
            except Exception as exc:
                session.rollback()
                print(f'Error: {exc}')

    def get_all_statistics():
        return session.query(Statistics).all()
    
    def get_statistic_by_id(stat_id):
        return session.query(Statistics).filter(Statistics.stat_id == stat_id).first()
    
    def get_player_statistics(player_id):
        return session.query(Statistics).filter(Statistics.player_id == player_id).all()

    def get_game_statistics(game_id):
        return session.query(Statistics).filter(Statistics.game_id == game_id).all()
    
    @classmethod
    def get_stat_with_highest(cls, attribute):
        valid_attributes = ['points_scored', 'rebounds', 'assists', 'steals', 'blocks']

        if attribute not in valid_attributes:
            print("Invalid attribute. Please provide one of: 'points_scored', 'rebounds', 'assists', 'steals', 'blocks'")
        else:
            highest_value = session.query(func.max(getattr(cls, attribute))).scalar()
            return session.query(cls).filter(getattr(cls, attribute) == highest_value).all()

    @classmethod
    def get_stat_with_lowest(cls, attribute):
        valid_attributes = ['points_scored', 'rebounds', 'assists', 'steals', 'blocks']

        if attribute not in valid_attributes:
            print("Invalid attribute. Please provide one of: 'points_scored', 'rebounds', 'assists', 'steals', 'blocks'")
        else:
            lowest_value = session.query(func.min(getattr(cls, attribute))).scalar()
            return session.query(cls).filter(getattr(cls, attribute) == lowest_value).all()


        
    def update_statistic(stat_id):
        if stat := Statistics.get_statistic_by_id(stat_id):
            try:
                new_player_id = input("Enter the new Player ID(leave empty to keep current): ")
                new_game_id = input("Enter the new Game ID(leave empty to keep current): ")
                new_points_scored = input("Enter the new number of Points Scored(leave empty to keep current): ")
                new_rebounds = input("Enter the new number of rebounds(leave empty to keep current): ")
                new_assists = input("Enter the new number of assists(leave empty to keep current): ")
                new_steals = input("Enter the new number of steals(leave empty to keep current): ")
                new_blocks = input("Enter the new number of blocks(leave empty to keep current): ")

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
        if stat := Statistics.get_statistic_by_id(stat_id):
            try:
                session.delete(stat)
                session.commit()
                print("Statistic successfully deleted:\n",{stat})
            except Exception as exc:
                session.rollback()
                print(f"Error deleting statistic: {exc}")
        else:
            print(f"Stats if ID {stat_id} not found")