from helpers import *

def main():
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
            pass
        elif choice == "9":
            pass
        elif choice == "10":
            pass
        elif choice == "11":
            pass
        elif choice == "12":
            pass
        elif choice == "13":
            pass
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit Program!!!")
    print("***********************Players Interactions***********************")
    print("1. Add a Player")
    print("2. List all Players")
    print("3. Get Player by ID")
    print("4: Get player by First Name")
    print("5: List of Players in a Team")
    print("6: Update Player details")
    print("7. Delete a Player")
    print("***********************Teams Interactions***********************")
    print("8. Add a Team")
    print("9. ")
    print("10: ")
    print("11: ")
    print("12: ")
    print("13: ")
    print("***********************Statistics Interactions***********************")
    print("8. ")
    print("9. ")
    print("10: ")
    print("11: ")
    print("12: ")
    print("13: ")

if __name__ == '__main__':
    print('Welcome to the Basketball Managment System!!!')
    main()