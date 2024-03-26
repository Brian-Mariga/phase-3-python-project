# lib/models/player.py

import logging
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Date, Time
from sqlalchemy.orm import relationship
from models.__init__ import Base, session


logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class Player(Base):

    __tablename__ = 'players'

    player_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    jersey_number = Column(Integer, nullable=False)
    contact_details = Column(String, nullable=False, unique=True)
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    team = relationship("Team", back_populates="players")
    statistics = relationship("Statistics", back_populates="player")

    __table_args__ = (
        UniqueConstraint('first_name', 'last_name', name='unique_player_name'),
    )

    # def __repr__(self):
    #     return f"<Player(id={self.player_id}, name={self.first_name} {self.last_name}, jersey={self.jersey_number})>"

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
        return session.query(Player).all()

    def get_player_by_id(player_id):
        return session.query(Player).filter(Player.player_id == player_id).first()

    
    def get_player_by_first_name(first_name):
        return session.query(Player).filter(Player.first_name == first_name).all()
    
    def get_players_of_a_team(team_id):
        return session.query(Player).filter(Player.team_id == team_id).all()

    
    def update_player(player_id):
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
                print("Player details updated successfully:")
                print(f"ID: {player.player_id}, Names: {player.first_name} {player.last_name}, Jersey Number: {player.jersey_number}, Contacts: {player.contact_details}, Team ID: {player.team_id}")

            except Exception as exc:
                session.rollback()
                print(f'Error updating player details: {exc}')

        else:
            print(f'Player with id {player_id} not found')

    def delete_player(player_id):
        if player := Player.get_player_by_id(player_id):
            try:
                session.delete(player)
                session.commit()
                print("Successfully deleted player:")
                print(f"ID: {player.player_id}, Names: {player.first_name} {player.last_name}, Jersey Number: {player.jersey_number}, Contacts: {player.contact_details}, Team ID: {player.team_id}")

            except Exception as exc:
                session.rollback()
                print(f'Error deleting player: {exc}')

        else:
            print(f'Player {player_id} not found')