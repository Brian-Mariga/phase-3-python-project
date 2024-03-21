# lib/models/player.py

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import relationship
from models.__init__ import Base, session

class Player(Base):

    __tablename__ = 'players'

    player_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    jersey_number = Column(Integer, nullable=False, unique=True)
    contact_details = Column(String, nullable=False, unique=True)
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    team = relationship("Teams", back_populates="players")

    def add_player(first_name, last_name, jersey_number, contact_details, team_id):
        if not first_name or not last_name or not jersey_number or not contact_details or not team_id:
            print("First Name, Last Name, Jersey number, Contact Details and Team id are required")
        
        else:
            new_player = Player(first_name = first_name,
                                last_name = last_name,
                                jersey_number = jersey_number,
                                contact_details = contact_details,
                                team_id = team_id)
            try:
                session.add(new_player)
                session.commit()
                print("Player added successfully")

            except Exception as exc:
                session.rollback()
                print(f'Error: {exc}')

    def get_all_players():
        players = session.query(Player).all()

        for player in players:
            print(player)
    
    def get_player_by_id(player_id):
        return session.query(Player).filter(Player.player_id == player_id).first()
    
    def get_player_by_first_name(first_name):
        players = session.query(Player).filter(Player.first_name == first_name).all()
        
        for player in players:
            print(player)
    
    def get_players_of_a_team(team_id):
        players =session.query(Player).filter(Player.team_id == team_id).all()

        for player in players:
            print(player)
    
    def update_player_details():
        player_id = input("Enter the player's id: ")

        if player := Player.get_player_by_id(player_id):
            try:
                new_first_name = input("Enter the player's new first name (leave empty to keep current): ")
                new_last_name = input("Enter the player's new last name (leave empty to keep current): ")
                new_jersey_number = input("Enter the player's new jersey number (leave empty to keep current): ")
                new_contact_details = input("Enter the player's new contact details (leave empty to keep current): ")
                new_team_id = input("Enter the player's new team id (leave empty to keep current): ")

                if new_first_name:
                    player.first_name = new_first_name
                if new_last_name:
                    player.last_name = new_last_name
                if new_jersey_number:
                    player.jersey_number = new_jersey_number
                if new_contact_details:
                    player.contact_details = new_contact_details
                if new_team_id:
                    player.team_id = new_team_id

                session.commit()
                print("Player details updated successfully:\n", {player})

            except Exception as exc:
                session.rollback()
                print(f'Error updating player details: {exc}')

        else:
            print(f'Player with id {player_id} not found')

    def delete_player():
        player_id = input("Enter the player's id: ")

        if player := Player.get_player_by_id(player_id):
            try:
                session.delete(player)
                session.commit()
                print("Successfully deleted player:\n",{player})

            except Exception as exc:
                session.rollback()
                print(f'Error deleting player: {exc}')

            else:
                print(f'Player {player_id} not found')