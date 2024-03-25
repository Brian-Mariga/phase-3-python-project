# lib/models/game.py

from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from models.__init__ import Base, session

class Game(Base):
    __tablename__ = 'games'

    game_id = Column(Integer, primary_key=True)
    home_team_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    away_team_id = Column(Integer, ForeignKey('teams.team_id'), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    location = Column(String, nullable=False)
    statistics = relationship("Statistics", back_populates="game")
    home_team = relationship("Team", foreign_keys=[home_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])

    __table_args__ = (
        UniqueConstraint('date', 'time', 'location', name='unique_game_details'),
    )

    @classmethod
    def create_game(cls, home, away, date, time, location):
        if not all([home, away, date, time, location]):
            print("All fields are required!")
            return
        else:
            try:
                new_game = cls(home=home, away=away, date=date, time=time, location=location)
                session.add(new_game)
                session.commit()
                print('Game added successfully')
            except Exception as exc:
                session.rollback()
                print(f'Error: {exc}')

    @classmethod
    def get_all_games(cls):
        return session.query(cls).all()
    
    @classmethod
    def get_game_by_id(cls, game_id):
        return session.query(cls).filter(cls.game_id == game_id).first()
    
    @classmethod
    def get_games_by_date(cls, date):
        return session.query(cls).filter(cls.date == date).all()
    
    @classmethod
    def get_games_by_team(cls, team_name):
        return session.query(cls).filter((cls.home == team_name) | (cls.away == team_name)).all()
    
    @classmethod
    def update_game(cls):
        game_id = input("Enter the game's id: ")

        if game := cls.get_game_by_id(game_id):
            try:
                new_home = input("Enter the new home team (leave empty to keep current): ")
                new_away = input("Enter the new away team (leave empty to keep current): ")
                new_date = input("Enter the new date (leave empty to keep current): ")
                new_time = input("Enter the new time (leave empty to keep current): ")
                new_location = input("Enter the new location (leave empty to keep current): ")

                if new_home:
                    game.home = new_home
                if new_away:
                    game.away = new_away
                if new_date:
                    game.date = new_date
                if new_time:
                    game.time = new_time
                if new_location:
                    game.location = new_location

                session.commit()
                print("Game details updated successfully:\n", {game})

            except Exception as exc:
                session.rollback()
                print(f'Error updating game details: {exc}')

        else:
            print(f'Game with id {game_id} not found')

    @classmethod
    def delete_game(cls):
        game_id = input("Enter the game's ID: ")

        if game := cls.get_game_by_id(game_id):
            try:
                session.delete(game)
                session.commit()
                print("Successfully deleted game:\n", game)

            except Exception as exc:
                session.rollback()
                print(f'Error deleting game: {exc}')

        else:
            print(f'Game with ID {game_id} not found')
