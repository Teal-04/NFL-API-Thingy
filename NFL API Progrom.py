from time import sleep
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

        print("Choose from the available options:")
        print("1. Live Game Stats")
        print("?. Filler")
        print("?. Filler")
        print("?. Filler")
        print("?. Filler")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            live_game_stat()
        elif choice == "2":
            exit()
menu()

def live_game_stat():

    return