#..................................imports.........................
import json
import os
from datetime import date
#...............................path.................................
path = "/storage/emulated/0/Python learning/things made by Siddharth/project.txt"
#...............................data handling.....................
def load_data():
    if os.path.exists(path):
        with open(path, "r") as file:
            return json.load(file)
    else:
        return {}

def save_data(data):
    with open(path, "w") as file:
        json.dump(data, file, indent = 4)
#................................core features.........................
def add_player(data, player):
    if player in data:
        print("This player already exists")
        return
    else:
        data[player] = {
        "Score": 0,
        "Last done": ""
        }
        print("Player added successfully")
        
def add_score(data, player, score):
    if player not in data:
        print("No such player")
        return
    else:
        today = str(date.today())
        if data[player]["Last done"] == today:
            print("Score already added")
            return
        else:
            data[player]["Score"] += score
            data[player]["Last done"] = today
            print("Score added")
def view_score(data, player):
    if player not in data:
        print("No such player")
        return
    else:
        print(f"\n{'PLAYER':<15} | {'SCORE':<10}")
        print("-"*28)
        print(f"{player:<15} | {data[player]["Score"]:<10}")
def reset_score(data, player):
    if player not in data:
        print("No such player")
        return
    else:
        data[player]["Score"] = 0
        print("Score reseted")
#............................menu.....................................
def menu():
    print("\n1) Add player")
    print("2) Add score")
    print("3) View score")
    print("4) Reset score")
    print("5) Exit")
    
    while True:
        user = input("Enter your choice: ")
        if user in ["1", "2", "3", "4", "5"]:
            return user
        else:
            print("Invalid choice")
#................................main...............................
def main():
    data = load_data()
    while True:
        choice = menu()
        if choice == "1":
            player = input("Enter player's name: ")
            add_player(data, player)
        elif choice == "2":
            player = input("Enter player's name: ")
            try:
                score = int(input("Enter score: "))
                add_score(data, player, score)
            except:
                print("Invalid score")
        elif choice == "3":
                player = input("Enter player's name: ")
                view_score(data, player)
        elif choice == "4":
              player = input("Enter player's name: ")
              reset_score(data, player)
        elif choice == "5":
              print("Bye")
              save_data(data)
              break
main()
        