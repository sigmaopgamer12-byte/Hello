#.......................................IMPORTS......................................
import os
import json
from datetime import date
import time
#......................................COLORS....................................
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"  
PURPLE = "\033[1;35m"
#................................FILE PATH.....................................
FILE_PATH = "/storage/emulated/0/Python learning/things made by Siddharth/info.txt"
#................................ID......................
active_quest_id = None
#.................................CLASS.....................................
class Game:
    #..................…...........DATA HANDLING..................
    def __init__(self):
        self.data = self.load_data()
        self.quests = {"Kill slime": 20, "Kill zombie": 50, "Kill wither": 100}
        self.quest_start_time = None
        self.quest_active = False
        self.active_quesr_id = None
    
    def load_data(self):
        if os.path.exists(FILE_PATH):
            try:
                with open(FILE_PATH, "r") as file:
                    content = file.read()
                    if not content:
                        return {}
                    return json.loads(content)
            except:
               return {}
        return {}
    
    def save_data(self):
        with open(FILE_PATH, "w") as file:
            json.dump(self.data, file, indent = 4)
    #..............................CORE FEATURES...............................
    def create_profile(self, name):
        if name in self.data:
            print(f"{RED}This profile already exists{RESET}")
            return
        self.data[name] = {
        "Name": name,
        "Level": 0,
        "Exp": 0
        }
        print(f"{GREEN}Profile successfully created{RESET}")
        self.save_data()
    def start_quests(self, name, choice_quest):
        if name not in self.data:
            print(f"{RED}No such profile{RESET}")
            return
        if self.quest_active:
            print(f"{RED}One quest already active{RESET}")
            return
        if choice_quest == "1":
            if not self.quest_active:
                print(f"Quest started: {choice_quest}")
                self.quest_start_time = time.time()
                self.quest_active = True
                print("Comeback after the mentioned time")
        elif choice_quest == "2":
            if not self.quest_active:
                print(f"Quest started: {choice_quest}")
                self.quest_start_time = time.time()
                self.quest_active = True
                print("Comeback after the mentioned time")
        elif choice_quest == "3":
            if not self.quest_active:
                print(f"Quest started: {choice_quest}")
                self.quest_start_time = time.time()
                self.quest_active = True
                print("Comeback after the mentioned time")
            
    def check_quest(self, name, choice_quest_check):
        if name not in self.data:
            print(f"{RED}No such profile{RESET}")
            return
        if not self.quest_active:
            print(f"{RED}No active quest{RESET}")
            return
        elapsed = time.time() - self.quest_start_time
        
        if choice_quest_check == "1":
            if elapsed >= 120:
                print(f"{GREEN}Quest completed{RESET}")
                self.data[name]["Exp"] += 20
                self.quest_active = False
                self.save_data()
            else:
                remaining = 120 - elapsed
                print(f"Still killing slimes......wait{int(remaining)} seconds")
        elif choice_quest_check == "2":
            if elapsed >= 300:
                print(f"{GREEN}Quest completed{RESET}")
                self.data[name]["Exp"] += 50
                self.quest_active = False
                self.save_data()
            else:
                remaining = 300 - elapsed
                print(f"Still killing zombies......wait{int(remaining)} seconds")
        elif choice_quest_check == "3":
            if elapsed >= 600:
                print(f"{GREEN}Quest completed{RESET}")
                self.data[name]["Exp"] += 100
                self.quest_active = False
                self.save_data()
            else:
                remaining = 600 - elapsed
                print(f"Still killing withers......wait{int(remaining)} seconds")
    
    def view_exp(self, name):
        if name not in self.data:
            print(f"{RED}No such profile{RESET}")
            return
        print("You level up on every 100 exp")
        print(f"{PURPLE}{'NAME':<15} | {'EXP':<12}{RESET}")
        print(f"{YELLOW}{name:<15} | {self.data[name]["Exp"]}{RESET}")
        
    def view_level(self, name):
        if name not in self.data:
            print(f"{RED}No such profile{RESET}")
            return
        print("You level up on every 100 exp")
        print(f"{PURPLE}{'NAME':<15} | {'LEVEL':<12}{RESET}")
        print(f"{YELLOW}{name:<15} | {self.data[name]["Level"]}{RESET}")
    
    def increase_level(self, name):
        if self.data[name]["Exp"] >= 100:
            self.data[name]["Level"] += 1
            self.data[name]["Exp"] -= 100
#..................................MAIN......................................
game = Game()
while True:
    print(CYAN, end = "")
    print("\n1) Create profile")
    print("2) Do quest")
    print("3) Check quest")
    print("4) Check exp")
    print("5) Check level")
    print("6) Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter your name: ")
        game.create_profile(name)
    
    elif choice == "2":
        name = input("Enter your name: ")
        print("Choose one of the quests bellow")
        print("\n1) Kill slimes: 20 exp, 2 minutes")
        print("2) Kill zombies: 50 exp, 5 minutes")
        print("3) Kill wither: 100 exp, 10 minutes")
        
        choice_quest = input("Enter your choice: ")
        
        if choice_quest in ["1", "2", "3"]:
            active_quest_id = choice_quest
            game.start_quests(name, choice_quest)
        
    elif choice == "3":
        name = input("Enter your name: ")
        print("Choose one of the quests bellow")
        print("\n1) Kill slimes: 20 exp, 2 minutes")
        print("2) Kill zombies: 50 exp, 5 minutes")
        print("3) Kill wither: 100 exp, 10 minutes")
        
        choice_quest_check = input("Enter your choice: ")
        
        if choice_quest_check == active_quest_id:
                game.check_quest(name, choice_quest_check)
                self.increase_level(name)
        else:
                print(f"{RED}Error{RESET}")
                
    elif choice == "4":
        name = input("Enter your name: ")
        game.view_exp(name)
    
    elif choice == "5":
        name = input("Enter your name: ")
        game.view_level(name)
    
    elif choice == "6":
        print("Bye")
        break