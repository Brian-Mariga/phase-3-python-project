# lib/seed.py

import logging
from models.player import Player
from models.team import Team
from models.game import Game
from models.statistics import Statistics
from datetime import date, time

def setup_logging():
    logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)

def seed_data():
    # Seed Players
    players_data = [
        {"first_name": "LeBron", "last_name": "James", "jersey_number": 23, "contact_details": "lebron@example.com", "team_id": 1},
        {"first_name": "Kevin", "last_name": "Durant", "jersey_number": 7, "contact_details": "kdurant@example.com", "team_id": 2},
        {"first_name": "Stephen", "last_name": "Curry", "jersey_number": 30, "contact_details": "scurry@example.com", "team_id": 3},
        {"first_name": "Giannis", "last_name": "Antetokounmpo", "jersey_number": 34, "contact_details": "giannis@example.com", "team_id": 4}
    ]
    for player_data in players_data:
        try:
            Player.add_player(**player_data)
        except Exception as e:
            print(f"Error adding player: {e}")

    # Seed Teams
    teams_data = [
        {"team_name": "Los Angeles Lakers"},
        {"team_name": "Brooklyn Nets"},
        {"team_name": "Golden State Warriors"},
        {"team_name": "Milwaukee Bucks"}
    ]
    for team_data in teams_data:
        try:
            Team.add_team(**team_data)
        except Exception as e:
            print(f"Error adding team: {e}")

    # Seed Games
    games_data = [
    {"home_team_id": 1, "away_team_id": 2, "date": date(2024, 4, 1), "time": time(19, 0), "location": "Staples Center"},
    {"home_team_id": 3, "away_team_id": 4, "date": date(2024, 4, 2), "time": time(20, 0), "location": "Chase Center"},
    {"home_team_id": 2, "away_team_id": 4, "date": date(2024, 4, 3), "time": time(18, 0), "location": "Barclays Center"},
    {"home_team_id": 1, "away_team_id": 3, "date": date(2024, 4, 4), "time": time(19, 30), "location": "Oracle Arena"}
    ]
    for game_data in games_data:
        try:
            Game.create_game(home_team_id=game_data["home_team_id"], away_team_id=game_data["away_team_id"],
                             date=game_data["date"], time=game_data["time"], location=game_data["location"])
        except Exception as e:
            print(f"Error adding game: {e}")

    # Seed Statistics
    statistics_data = [
        {"player_id": 1, "game_id": 1, "points_scored": 25, "rebounds": 8, "assists": 7, "steals": 2, "blocks": 1},
        {"player_id": 2, "game_id": 2, "points_scored": 30, "rebounds": 5, "assists": 9, "steals": 3, "blocks": 2},
        {"player_id": 3, "game_id": 3, "points_scored": 35, "rebounds": 4, "assists": 11, "steals": 4, "blocks": 1},
        {"player_id": 4, "game_id": 4, "points_scored": 28, "rebounds": 12, "assists": 6, "steals": 3, "blocks": 3}
    ]
    for statistic_data in statistics_data:
        try:
            Statistics.add_statistics(**statistic_data)
        except Exception as e:
            print(f"Error adding statistics: {e}")

if __name__ == "__main__":
    setup_logging()
    seed_data()