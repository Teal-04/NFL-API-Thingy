from time import sleep
from team_abbreviations import team_abbreviations
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def menu():
    while True:
        print("Welcome")

        sleep(2.5)

        for i in range(1, 30):
            print("")

        print("This Program will allow you to harness the power of technology to see various stats about the NFL. Includes:")
        print("*Live Stat Coverage")
        print("*Filler")
        print("*Filler")
        print("*Filler")
        print("*Filler")
        print("*Filler")
        print("*Filler")
        print("*And more soon to come!")
        sleep(8)

        for i in range(1, 30):
            print("")
        menu_choices()

def menu_choices():
    while True:
        print("Choose from the available options:")
        print("1. Live Game Stats")
        print("?. Filler")
        print("?. Filler")
        print("?. Filler")
        print("?. Filler")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            live_game_menu()
        elif choice == "2":
            exit()
        else:
            print("")
            print("Invalid choice, try again please")
            sleep(2)
            for i in range(1, 10):
                print("")



def live_game_menu():
    while True:
        print("\n--- Live Game Stats Menu ---")
        print("1. View Team Abbreviations")
        print("2. View Live Game Info")
        print("3. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_team_abbreviations()
        elif choice == "2":
            view_live_game_info()
        elif choice == "3":
            return
        else:
            print("Invalid option. Please try again.")

def show_team_abbreviations():
    print("\n--- List of NFL Team Abbreviations ---")
    for abbr, team_name in team_abbreviations.items():
        print(f"{abbr}: {team_name}")
    print("\n")

def view_live_game_info():
    print("")



if __name__ == "__main__":
    menu()