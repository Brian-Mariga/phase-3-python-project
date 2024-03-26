# lib/models/game.py

from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from models.__init__ import Base, session
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from models.team import Team

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
    def create_game(cls, home_team_id, away_team_id, date, time, location):
        home_team_id = int(home_team_id)
        away_team_id = int(away_team_id)

        if not all([home_team_id, away_team_id, date, time, location]):
            print("All fields are required!")
            return
        elif home_team_id == away_team_id:
            print("Home team cannot be the same as away team!")
            return
        elif session.query(Team).filter(Team.team_id == home_team_id).first() is None or session.query(Team).filter(Team.team_id == away_team_id).first() is None:
            print("Home team ID and Away Team ID must be instances in Teams Table")
            return

        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            time = datetime.strptime(time, '%H:%M').time()
            new_game = cls(home_team_id=home_team_id, away_team_id=away_team_id, date=date, time=time, location=location)
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
    def get_games_by_team(cls, team_id):
        return session.query(cls).filter((cls.home_team_id == team_id) | (cls.away_team_id == team_id)).all()
    
    @classmethod
    def update_game(cls,game_id):
        if game := cls.get_game_by_id(game_id):
            try:
                new_home_team_id = input("Enter the new home team (leave empty to keep current): ")
                new_away_team_id = input("Enter the new away team (leave empty to keep current): ")
                new_date = input("Enter the new date (leave empty to keep current): ")
                new_time = input("Enter the new time (leave empty to keep current): ")
                new_location = input("Enter the new location (leave empty to keep current): ")


                if new_home_team_id:
                    game.home = new_home_team_id
                if new_away_team_id:
                    game.away = new_away_team_id
                if new_date:
                    new_date = datetime.strptime(new_date, '%Y-%m-%d').date()
                    game.date = new_date
                if new_time:
                    new_time = datetime.strptime(new_time, '%H:%M').time()
                    game.time = new_time
                if new_location:
                    game.location = new_location

                session.commit()
                print("Game details updated successfully:")
                print(f"Game ID: {game.game_id} Home Team ID: {game.home_team_id} Away Team ID: {game.away_team_id} Date: {game.date} Time: {game.time} Location: {game.location}")

            except Exception as exc:
                session.rollback()
                print(f'Error updating game details: {exc}')

        else:
            print(f'Game with id {game_id} not found')

    @classmethod
    def delete_game(cls,game_id):
        if game := cls.get_game_by_id(game_id):
            try:
                session.delete(game)
                session.commit()
                print("Successfully deleted game: ")
                print(f"Game ID: {game.game_id} Home Team ID: {game.home_team_id} Away Team ID: {game.away_team_id} Date: {game.date} Time: {game.time} Location: {game.location}")

            except Exception as exc:
                session.rollback()
                print(f'Error deleting game: {exc}')

        else:
            print(f'Game with ID {game_id} not found')
