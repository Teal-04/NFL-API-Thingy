from time import sleep
from team_abbreviations import team_abbreviations
from dotenv import load_dotenv
import os
import requests
# Just want to shout out the amazing people who use Stack Overflow. I have learned more than I ever imagined I would on that website
# Bless everyone who posts on there, this wouldn't be possible without y'all <3

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
        print("*Player Information")
        print("*Team Information")
        print("*Injury Details")
        print("*Seasonal Stat Leaders")
        print("*Filler")
        print("*Filler")
        print("*And more soon to come!")
        sleep(6.25)
        for i in range(1, 30):
            print("")
        menu_choices()

def menu_choices():
    while True:
        print("Choose from the available options:")
        print("1. Live Game Stats (W.I.P)")
        print("2. Player Profile")
        print("3. Team Profile")
        print("4. Injury Report")
        print("5. Seasonal Stat Information")
        print("?. Filler")
        print("?. Filler")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for i in range(1, 10):
                print("")
            live_game_menu()
        elif choice == "2":
            for i in range(1, 10):
                print("")
            player_profile()
        elif choice == "3":
            for i in range(1, 10):
                print("")
            team_profile()
        elif choice == "4":
            for i in range(1, 10):
                print("")
            injury_report()
        elif choice == "5":
            seasonal_stat_leader()
        elif choice == "6":
            exit()
        else:
            print("")
            print("Invalid choice, try again please dear god")
            sleep(2)
            for i in range(1, 10):
                print("")

# ***************************
# DIVIDER FOR LIVE GAME STUFF
# ***************************

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
            print("Invalid choice, its 1-3 -_-")
            sleep(2)
            for i in range(1, 10):
                print("")

def show_team_abbreviations():
    print("\n--- List of NFL Team Abbreviations ---")
    for abbr, team_name in team_abbreviations.items():
        print(f"{abbr}: {team_name}")
    sleep(2)
    print("\n")

def view_live_game_info():
    print("")

# **************************
# DIVIDER FOR PLAYER PROFILES
# **************************

def fetch_player_profiles():
    url = f"https://api.sportsdata.io/v3/nfl/scores/json/Players?key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching player profiles: {response.status_code}")
        return None

def player_profile():
    player_name = input("Enter the player's name: ").lower()

    profiles = fetch_player_profiles()

    if profiles:
        found_profiles = [profile for profile in profiles if player_name in profile['Name'].lower()]
        if found_profiles:
            for profile in found_profiles:
                display_player_profile(profile)
        else:
            print("Player not found. Please try again.")
    else:
        print("Could not retrieve player data.")

def display_player_profile(profile):
    print("\n--- Player Profile ---")
    print(f"Name: {profile['Name']}")
    print(f"Team: {profile['Team']}")
    print(f"Position: {profile['Position']}")
    print(f"Height: {profile['Height']}")
    print(f"Weight: {profile['Weight']}")
    print(f"College: {profile['College']}")
    print(f"Experience: {profile['Experience']} years")
    print("-" * 40)

# ************************
# DIVIDER FOR TEAM PROFILE
# ************************

def fetch_team_data():
    url = f"https://api.sportsdata.io/v3/nfl/scores/json/Teams?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching team data.")
        return None

def display_team_profile(team_data):
    if team_data:
        print(f"Team Name: {team_data['FullName']}")
        print(f"Conference: {team_data['Conference']}")
        print(f"Division: {team_data['Division']}")
        print(f"Stadium: {team_data['StadiumDetails']['Name']}")
        print(f"Head Coach: {team_data['HeadCoach']}")
        print(f"Offensive Scheme: {team_data['OffensiveScheme']}")
        print(f"Defensive Scheme: {team_data['DefensiveScheme']}")
        print("")
    else:
        print("Team not found.")

def team_profile():
    while True:
        print("\nTeam Profile Menu:")
        print("1. View Team Abbreviations")
        print("2. Search Team Profile")
        print("3. Exit to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_team_abbreviations()
        elif choice == "2":
            teams_data = fetch_team_data()
            if teams_data:
                team_abbreviation = input("Enter the team abbreviation: ").upper()
                team_data = next((team for team in teams_data if team["Key"] == team_abbreviation), None)
                display_team_profile(team_data)
        elif choice == "3":
            for i in range(1, 10):
                print("")
            break
        else:
            print("Invalid choice, its 1-3 -_-")
            sleep(2)
            for i in range(1, 10):
                print("")

# *************************
# DIVIDER FOR INJURY REPORT
# *************************

def fetch_injury_report(season, week):
    url = f"https://api.sportsdata.io/v3/nfl/stats/json/Injuries/{season}/{week}?key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching injury report: {response.status_code}")
        return None

def display_injury_report(injuries, team_abbr):
    team_injuries = [injury for injury in injuries if injury['Team'] == team_abbr]
    if team_injuries:
        for injury in team_injuries:
            print(f"Player: {injury['Name']}")
            print(f"Position: {injury['Position']}")
            # print(f"Injury: {injury['BodyPart']} - Status: {injury['Status']}") #<-- If you have paid version of API uncomment this
            print(f"Last Updated: {injury['Updated']}")
            print("-" * 30)
    else:
        print(f"No injuries found for the {team_abbr}")

def injury_report():
    season = input("Enter the season (e.g: 2023REG): ")
    week = input("Enter the week (e.g: 5): ")
    team_abbr = input("Enter the team abbreviation: ").upper()

    injuries = fetch_injury_report(season, week)
    if injuries:
        display_injury_report(injuries, team_abbr)

# ******************************
# DIVIDER FOR SEASONAL STAT INFO
# ******************************

def fetch_stat_leaders(season):
    print("Waiting....")
    url = f"https://api.sportsdata.io/v3/nfl/stats/json/PlayerSeasonStats/{season}?key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data...")
        return None

def display_stat_leaders(stat_leaders):
    print("Top Passing Yards Leaders:")
    for player in sorted(stat_leaders, key=lambda x: x['PassingYards'], reverse=True)[:5]: # I don't quite get this, but all I know is lambda is thumbs up
        print(f"{player['Name']}: {player['PassingYards']} yards")

    print("\nTop Rushing Yards Leaders:")
    for player in sorted(stat_leaders, key=lambda x: x['RushingYards'], reverse=True)[:5]:
        print(f"{player['Name']}: {player['RushingYards']} yards")

    print("\nTop Receptions Leaders:")
    for player in sorted(stat_leaders, key=lambda x: x['Receptions'], reverse=True)[:5]:
        print(f"{player['Name']}: {player['Receptions']} receptions")

    print("\nTop Sack Leaders:")
    sack_leaders = sorted(stat_leaders, key=lambda x: x.get('Sacks', 0), reverse=True)[:5]
    for player in sack_leaders:
        print(f"{player['Name']}: {player['Sacks']} sacks")

    print("\nTop Interception Leaders:")
    interception_leaders = sorted(stat_leaders, key=lambda x: x.get('Interceptions', 0), reverse=True)[:5]
    for player in interception_leaders:
        print(f"{player['Name']}: {player['Interceptions']} interceptions")

    print("")
    sleep(4)

def seasonal_stat_leader():
    season = input("Enter the season year (e.g: 2023): ")
    stat_leaders = fetch_stat_leaders(season)

    if stat_leaders:
        display_stat_leaders(stat_leaders)
    else:
        print("Noting here.")

# ***********
# PLACEHOLDER
# ***********


if __name__ == "__main__":
    menu()