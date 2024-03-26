# lib/helpers.py

import logging
import sqlalchemy as sa
from models.player import Player
from models.team import Team
from models.game import Game
from models.statistics import Statistics
from models.__init__ import session
import sys

class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno != logging.INFO

# Create a logger and set its level to WARNING
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

# Add the custom filter to the logger
logger.addFilter(InfoFilter())

# Disable SQLAlchemy logging
sa_log = logging.getLogger('sqlalchemy.engine')
sa_log.setLevel(logging.WARNING)

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
            # team_name = Team.get_team_name_by_id(player.team_id)
            print(f"ID: {player.player_id}, Names: {player.first_name} {player.last_name}, Jersey Number: {player.jersey_number}, Contacts: {player.contact_details}, Team ID: {player.team_id}")
            print()
    else:
        print("No player found")

def get_player_by_player_id():
    player_id = input("Enter the Player's id: ")

    if player := Player.get_player_by_id(player_id):
        team_name = Team.get_team_name_by_id(player.team_id)
        print(f"Details for player of ID {player_id}")
        print(f"ID: {player.player_id}, Names: {player.first_name} {player.last_name}, Jersey Number: {player.jersey_number}, Contacts: {player.contact_details}, Team ID: {player.team_id}, Team Name: {team_name}")
    else:
        print(f"Player of id {player_id} not found")

def get_a_player_by_player_first_name():
    first_name = input("Enter the Player's first name: ")

    if players := Player.get_player_by_first_name(first_name):
        for player in players:
            team_name = Team.get_team_name_by_id(player.team_id)
            print(f"ID: {player.player_id}, Names: {player.first_name} {player.last_name}, Jersey Number: {player.jersey_number}, Contacts: {player.contact_details}, Team ID: {player.team_id}, Team Name: {team_name}")
            print()
    else:
        print(f"Player of name {first_name} not found")

def list_of_players_of_a_team():
    team_id = input("Enter Team's id: ")
    if players := Player.get_players_of_a_team(team_id):
        print(f"Players of the team with ID {team_id}")
        for player in players:
            # team_name = Team.get_team_name_by_id(player.team_id)
            print(f"ID: {player.player_id}, Names: {player.first_name} {player.last_name}, Jersey Number: {player.jersey_number}, Contacts: {player.contact_details}, Team ID: {player.team_id}")
            print()
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
        print("List of all teams:")
        for team in teams:
            print(f"ID: {team.team_id}, Name: {team.team_name}")
            print()
    else:
        print("No team found")

def list_team_by_id():
    team_id = input("Enter Team ID: ")
    if team := Team.get_team_by_id(team_id):
        print(f"ID: {team.team_id}, Name: {team.team_name}")
    else:
        print(f"Player of id {team_id} not found")

def list_team_by_name():
    team_name = input("Enter Team name: ")
    if team := Team.get_team_by_name(team_name):
        print(f"ID: {team.team_id}, Name: {team.team_name}")
    else:
        print(f"Team of name {team_name} not found")

def update_a_team():
    team_id = input('Enter the team id: ')
    Team.update_team(team_id)

def delete_a_team():
    team_id = input('Enter the team id: ')
    Team.delete_team(team_id)


def create_a_new_game():
    home = input("Enter the Home Team ID: ")
    away = input("Enter the Away Team ID: ")
    date = input("Enter the Date of the game in the format 'YYYY-MM-DD': ")
    time = input("Enter the Game's time in the format 'HH:MM': ")
    location = input("Enter the location of the Game: ")

    Game.create_game(home, away, date, time, location)

def list_of_games():
    if games := Game.get_all_games():
        print("List of Games:")
        for game in games:
            print(f"Game ID: {game.game_id} Home Team ID: {game.home_team_id} Away Team ID: {game.away_team_id} Date: {game.date} Time: {game.time} Location: {game.location}")
            print()
    else:
        print("No games found")

def list_game_by_id():
    game_id = input("Enter the game ID: ")

    if game := Game.get_game_by_id(game_id):
        print(f"Game ID: {game.game_id} Home Team ID: {game.home_team_id} Away Team ID: {game.away_team_id} Date: {game.date} Time: {game.time} Location: {game.location}")
    else:
        print(f"Game of id {game_id} not found")

def list_games_by_date():
    date = input("Enter the Games' date in the format 'YYYY-MM-DD': ")

    if games := Game.get_games_by_date(date):
        for game in games:
            print(f"Game ID: {game.game_id} Home Team ID: {game.home_team_id} Away Team ID: {game.away_team_id} Date: {game.date} Time: {game.time} Location: {game.location}")
    else:
        print(f"No game of '{date}' found")

def list_games_by_team_id():
    team_id = input("Enter the Team's ID: ")

    if games := Game.get_games_by_team(team_id):
        for game in games:
            print(f"Game ID: {game.game_id} Home Team ID: {game.home_team_id} Away Team ID: {game.away_team_id} Date: {game.date} Time: {game.time} Location: {game.location}")
            print()
    else:
        print(f"Team of name '{team_id}' not found")

def update_a_game():
    game_id = input("Enter the Game's ID: ")
    Game.update_game(game_id)

def delete_a_game():
    game_id = input("Enter the Game's ID: ")
    Game.delete_game(game_id)



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
        print("List of stats:")
        for stat in stats:
            print(f"ID: {stat.stat_id}, Player ID: {stat.player_id}, Game ID: {stat.game_id}, Points Scored: {stat.points_scored}, Rebounds: {stat.rebounds}, Assists: {stat.assists}, Steals: {stat.steals}, Blocks: {stat.blocks}")
            print()
    else:
        print("No stats found")

def list_stat_by_id():
    stat_id = input("Enter the stat ID: ")
    if stat := Statistics.get_statistic_by_id(stat_id):
        print(f"ID: {stat.stat_id}, Player ID: {stat.player_id}, Game ID: {stat.game_id}, Points Scored: {stat.points_scored}, Rebounds: {stat.rebounds}, Assists: {stat.assists}, Steals: {stat.steals}, Blocks: {stat.blocks}")
    else:
        print(f"Stat of ID {stat_id} not found")

def list_player_stats():
    player_id = input("Enter the Player's ID: ")
    if stats := Statistics.get_player_statistics(player_id):
        print(f'Stats of Player of ID {player_id}')
        for stat in stats:
            print(f"ID: {stat.stat_id}, Player ID: {stat.player_id}, Game ID: {stat.game_id}, Points Scored: {stat.points_scored}, Rebounds: {stat.rebounds}, Assists: {stat.assists}, Steals: {stat.steals}, Blocks: {stat.blocks}")
            print()
    else:
        print(f"Stats of player of ID {player_id} not found")

def list_game_stats():
    game_id = input("Enter the Game ID: ")
    if stats := Statistics.get_game_statistics(game_id):
        print(f"Stats for game ID {game_id}:")
        for stat in stats:
            player = Player.get_player_by_id(stat.player_id)
            print(f"ID: {stat.stat_id}, Player ID: {stat.player_id}, Name: {player.first_name} {player.last_name}, Game ID: {stat.game_id}, Points Scored: {stat.points_scored}, Rebounds: {stat.rebounds}, Assists: {stat.assists}, Steals: {stat.steals}, Blocks: {stat.blocks}")
            print()
    else:
        print(f"Stats of Game ID {game_id} not found")

def list_highest_stat_of_a_field():
    field = input("Enter the field name.Must be either of('points_scored', 'rebounds', 'assists, steals', 'blocks'): ")
    if stats := Statistics.get_stat_with_highest(field):
        print(f"Highest {field}:")
        for stat in stats:
            print(f"Player ID: {stat.player_id}, Game ID: {stat.game_id}, {field.capitalize()}: {getattr(stat, field)}")
    else:
        print("No statistics found.")



def list_lowest_stat_of_a_field():
    field = input("Enter the field name.Must be either of('points_scored', 'rebounds', 'assists, steals', 'blocks'): ")
    if stats := Statistics.get_stat_with_lowest(field):
        print(f"Least {field}:")
        for stat in stats:
            print(f"Player ID: {stat.player_id}, Game ID: {stat.game_id}, {field.capitalize()}: {getattr(stat, field)}")
    else:
        print("No statistics found.")

def update_stat():
    stat_id = input("Enter stat ID: ")

    Statistics.update_statistic(stat_id)

def delete_stat():
    stat_id = input("Enter the stat ID: ")
    Statistics.delete_statistic(stat_id)