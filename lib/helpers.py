from models.player import Player
from models.team import Team
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
    if players := Player.get_all_players():
        for player in players:
            print(player)
    else:
        print("No player found")

def get_player_by_player_id():
    player_id = input("Enter the Player's id: ")

    if player := Player.get_player_by_id(player_id):
        print(player)
    else:
        print(f"Player of id {player_id} not found")

def get_a_player_by_player_first_name():
    first_name = input("Enter the Player's first name: ")

    if player := Player.get_player_by_first_name(first_name):
        print(player)
    else:
        print(f"Player of id {first_name} not found")

def list_of_players_of_a_team():
    team_id = input("Enter Team's id: ")
    if players := Player.get_players_of_a_team(team_id):
        for player in players:
            print(player)
    else:
        print(f"Team of id {team_id} not found")

def update_player_details():
    Player.update_player()

def delete_a_player():
    Player.delete_player()
    


def add_a_team():
    team_name = input("Enter the Team's name: ")
    Team.add_team(team_name)

def list_of_teams():
    if teams := Team.get_all_teams():
        for team in teams:
            print(team)
    else:
        print("No team found")

def list_team_by_id():
    team_id = input("Enter Team ID: ")
    if player := Team.get_team_by_id(team_id):
        print(player)
    else:
        print(f"Player of id {team_id} not found")

def list_team_by_name():
    team_name = input("Enter Team name: ")
    if player := Team.get_team_by_name(team_name):
        print(player)
    else:
        print(f"Player of id {team_name} not found")

def update_a_team():
    Team.update_team()

def delete_a_team():
    Team.delete_team()


def create_a_new_game():
    home = input("Enter the Home Team: ")
    away = input("Enter the Away Team: ")
    date = input("Enter the Date of the game in the format 'YYYY-MM-DD': ")
    time = input("Enter the Game's time in the format 'HH:MM': ")
    location = input("Enter the location of the Game: ")

    Game.create_game(home, away, date, time, location)

def list_of_games():
    if games := Game.get_all_games():
        for game in games:
            print(game)
    else:
        print("No games found")

def list_game_by_id():
    game_id = input("Enter the game ID: ")

    if game := Game.get_game_by_id(game_id):
        print(game)
    else:
        print(f"Game of id {game_id} not found")

def list_games_by_date():
    date = input("Enter the Games' date in the format 'YYYY-MM-DD': ")

    if games := Game.get_games_by_date(date):
        for game in games:
            print(game)
    else:
        print(f"No game of '{date}' found")

def list_games_by_team():
    team_name = input("Enter the Team's name: ")

    if team := Team.get_team_by_name(team_name):
        print(team)
    else:
        print(f"Team of name '{team_name}' not found")

def update_a_team():
    Team.update_team()

def delete_a_team():
    Team.delete_team()