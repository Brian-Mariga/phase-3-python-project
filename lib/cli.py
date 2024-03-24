# lib/cli.py

from helpers import *
from models.__init__ import create_tables

def main():
    create_tables()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_a_player()
        elif choice == "2":
            list_of_players()
        elif choice == "3":
            get_player_by_player_id()
        elif choice == "4":
            get_a_player_by_player_first_name()
        elif choice == "5":
            list_of_players_of_a_team()
        elif choice == "6":
            update_player_details()
        elif choice == "7":
            delete_a_player()
        elif choice == "8":
            add_a_team()
        elif choice == "9":
            list_of_teams
        elif choice == "10":
            list_team_by_id()
        elif choice == "11":
            list_team_by_name()
        elif choice == "12":
            update_a_team()
        elif choice == "13":
            delete_a_team()
        elif choice == "14":
            create_a_new_game()
        elif choice == "15":
            list_of_games()
        elif choice == "16":
            list_game_by_id()
        elif choice == "17":
            list_games_by_date()
        elif choice == "18":
            list_games_by_team()
        elif choice == "19":
            update_a_team()
        elif choice == "20":
            delete_a_team()
        elif choice == "21":
            create_statistic()
        elif choice == "22":
            list_all_statistics()
        elif choice == "23":
            list_stat_by_id()
        elif choice == "24":
            list_player_stats()
        elif choice == "25":
            list_game_stats()
        elif choice == "26":
            list_highest_stat_of_a_field()
        elif choice == "27":
            list_lowest_stat_of_a_field()
        elif choice == "28":
            update_stat()
        elif choice == "29":
            delete_stat()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit Program!!!")
    print("*************************Players Menu************************")
    print("1. Add a Player")
    print("2. List all Players")
    print("3. Get Player by ID")
    print("4: Get player by First Name")
    print("5: List of Players in a Team")
    print("6: Update Player details")
    print("7. Delete a Player")
    print("**************************Teams Menu*************************")
    print("8. Add a Team")
    print("9. List all teams")
    print("10: Get a Team by ID")
    print("11: Get a team by Name")
    print("12: Update Team details")
    print("13: Delete a Team")
    print("*************************Games Menu**************************")
    print("14: Add a Game ")
    print("15. List all Games")
    print("16: Get game by ID")
    print("17: Get game by date")
    print("18: Get game by team")
    print("19: Update Game details")
    print("20: Delete a game")
    print("***********************Statistics Menu***********************")
    print("21: Add a Statistic")
    print("22: List all statistics")
    print("23: Get a stat by ID")
    print("24: Get the stats of a Player")
    print("25: Get the stats of a Game")
    print("26: Get the highest stats by a field")
    print("27: Get the lowest stats by a field")
    print("28: Update a Stat Details")
    print("29: Delete a Stat")

if __name__ == '__main__':
    print('Welcome to the Basketball Managment System!!!')
    main()