# lib/helpers.py

from models.player import Player
from models.team import Team
from models.game import Game
from models.statistics import Statistics
from models.__init__ import session
import logging
import sys

logging.getLogger('sqlalchemy').setLevel(logging.WARNING)

def exit_program():
    print("Goodbye!")
    exit()

def add_a_player():
    first_name = input("Enter the Player's first name: ")
    last_name = input("Enter the Player's last name: ")
    jersey_number = input("Enter the Player's jersey number: ")
    contact_details = input("Enter the Player's contact details: ")
    team_id = input("Enter the Player's team id: ")

    if team := session.query(Team).filter_by(team_id = team_id).first():
        Player.add_player(first_name, last_name, jersey_number, contact_details, team_id)
    else:
        print("Error: Team with the provided team id does not exist.")

def list_of_players():
    if players := Player.get_all_players():
        for player in players:
            team_name = Team.get_team_name_by_id(player.team_id)
            print(f"ID: {player.player_id}, Names: {player.first_name} {player.last_name}, Jersey Number: {player.jersey_number}, Contacts: {player.contact_details}, Team ID: {player.team_id}, Team Name: {team_name}")
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
    player_id = input("Enter the player's id: ")
    Player.update_player(player_id)

def delete_a_player():
    player_id = input("Enter the player's id: ")
    Player.delete_player(player_id)
    


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
    team_id = input('Enter the team id: ')
    Team.update_team(team_id)

def delete_a_team():
    team_id = input('Enter the team id: ')
    Team.delete_team(team_id)


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

    if team := Game.get_games_by_team(team_name):
        print(team)
    else:
        print(f"Team of name '{team_name}' not found")

def update_a_team():
    team_id = input("Enter the Team's ID: ")
    Team.update_team(team_id)

def delete_a_team():
    team_id = input("Enter the Team's ID: ")
    Team.delete_team(team_id)



def create_statistic():
    player_id = input("Enter the player's ID: ")
    game_id = input("Enter the Game ID: ")
    points_scored = input("Enter the points: ")
    rebounds = input("Enter the number of rebounds: ")
    assists = input("Enter the number of assists: ")
    steals = input("Enter the number of steals: ")
    blocks = input("Enter the number of blocks: ")
    Statistics.add_statistics(player_id, game_id, points_scored, rebounds, assists, steals, blocks)

def list_all_statistics():
    if stats := Statistics.get_all_statistics():
        for stat in stats:
            print(stat)
    else:
        print("No stats found")

def list_stat_by_id():
    stat_id = input("Enter the stat ID: ")
    if stat := Statistics.get_statistic_by_id(stat_id):
        print(stat)
    else:
        print(f"Stat of ID {stat_id} not found")

def list_player_stats():
    player_id = input("Enter the Player's ID: ")
    if stats := Statistics.get_player_statistics(player_id):
        for stat in stats:
            print(stat)
    else:
        print(f"Stats of player of ID {player_id} not found")

def list_game_stats():
    game_id = input("Enter the Game ID: ")
    if stats := Statistics.get_game_statistics(game_id):
        for stat in stats:
            print(stat)
    else:
        print(f"Stats of Game ID {game_id} not found")

def list_highest_stat_of_a_field():
    field = input("Enter the field name.Must be either of('points_scored', 'rebounds', 'assists, steals', 'blocks'): ")

    Statistics.get_stat_with_highest(field)

def list_lowest_stat_of_a_field():
    field = input("Enter the field name.Must be either of('points_scored', 'rebounds', 'assists, steals', 'blocks'): ")

    Statistics.get_stat_with_lowest(field)

def update_stat():
    stat_id = input("Enter stat ID: ")

    Statistics.update_statistic(stat_id)

def delete_stat():
    stat_id = input("Enter the stat ID: ")
    Statistics.delete_statistic(stat_id)