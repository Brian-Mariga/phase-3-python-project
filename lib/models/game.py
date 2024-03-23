# lib/models/game.py

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import relationship
from models.__init__ import Base, engine,session

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

    def create_game(home, away, date, time, location):
        if not home or not away or not date or not time or not location:
            print('Home, Away, Date, Time and Location are required')
        else:
            try:
                new_game = Game(home=home, away= away, date=date, time=time,location= location)
                session.add(new_game)
                session.commit()
                print('Game added successfully')
            except Exception as exc:
                session.rollback()
                print(f'Error: {exc}')

    def get_all_games():
        return session.query(Game).all()
    
    def get_game_by_id(game_id):
        return session.query(Game).filter(Game.game_id == game_id).first()
    
    def get_games_by_date(date):
        return session.query(Game).filter(Game.date == date).all()
    
    def get_games_by_team(team_name):
        return session.query(Game).filter((Game.home == team_name) | (Game.away == team_name)).all()
    
    def update_game():
        game_id = input("Enter the game's id: ")

        if game := Game.get_game_by_id(game_id):
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

    def delete_game():
        game_id = input("Enter the game's ID: ")

        if game := Game.get_game_by_id(game_id):
            try:
                session.delete(game)
                session.commit()
                print("Successfully deleted game:\n", game)

            except Exception as exc:
                session.rollback()
                print(f'Error deleting game: {exc}')

        else:
            print(f'Game with ID {game_id} not found')