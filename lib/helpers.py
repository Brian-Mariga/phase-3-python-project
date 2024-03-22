from models.player import Player
from models.game import Game

def exit_program():
    print("Goodbye!")
    exit()

def add_a_player():
    first_name = input("Enter the Player's first name: ")
    last_name = input("Enter the Player's last name: ")
    jersey_number = input("Enter the Player's jersey number: ")
    contact_details = input("Enter the Player's contact details")
    team_id = input("Enter the Player's team id: ")

    Player.add_player(first_name, last_name, jersey_number, contact_details, team_id)

def list_of_players():
    players = Player.get_all_players()

    for player in players:
        print(player)

def get_player_by_player_id():
    player_id = input("Enter the Player's id: ")

    player = Player.get_player_by_id(player_id)
    print(player)

def get_a_player_by_player_first_name():
    first_name = input("Enter the Player's first name: ")

    player = Player.get_player_by_first_name(first_name)
    print(player)

def list_of_players_of_a_team():
    team_id = input("Enter Team's id: ")
    players = Player.get_players_of_a_team(team_id)
    for player in players:
        print(player)

def update_player_details():
    Player.update_player()

def delete_a_player():
    Player.delete_player()
    
