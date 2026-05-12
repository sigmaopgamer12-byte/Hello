#.....................................IMPORTS......................................
import os
import json
from datetime import date
#....................................COLORS........................................
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"  
PURPLE = "\033[1;35m"
#...................................FILE PATH......................................
FILE_PATH = "/storage/emulated/0/Python learning/things made by Siddharth/gym.txt"
#...............................DATA HANDLING...............................
def load_data():
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
   
def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent = 4)
#..............................CORE FEATURES..................................
def create_profile(data, dict_name, bmi):
    data[dict_name] = {
    "BMI": bmi,
    "Last done": str(date.today()),
    "Streak": 0,
    "Exercises": {}
    }
    print(f"{GREEN}Profile successfully created{RESET}")

def add_exercise(data, dict_name, exercise):
    data[dict_name]["Exercises"][exercise] = 0
    print(f"{GREEN}Exercise successfully added{RESET}")

def add_reps(data, dict_name, exercise, reps):
    data[dict_name]["Exercises"][exercise] += reps
    print(f"{GREEN}Reps added to exercise{RESET}")

def mark_done(data, dict_name):
    data[dict_name]["Streak"] += 1
    print(f"{GREEN} Successfully marked done now your streak is {data[dict_name]['Streak']}{RESET}")

def view_profile(data, dict_name):
    print(f"{GREEN}Showing the profile.......{RESET}")
    print("\n" + "="*60)
    print(f"{YELLOW}{'NAME':<20} | {'BMI':<15} | {'STREAK':<12} | {'LAST DONE':<8}")
    print("-"*60)
    print(f"{PURPLE}{dict_name:<20} | {data[dict_name]['BMI']:<15} | {data[dict_name]['Streak']:<12} | {data[dict_name]['Last done']:<8}")
    print(f"\n"+"="*60)
    exercises = data[dict_name].get("Exercises", {})
    if not exercises:
        print("No exercises")
    else:
        sorted_reps = sorted(exercises.items(), key = lambda x:x[1], reverse = True)
        print(f"{YELLOW}Showing exercises and reps{RESET}")
        for name, reps in sorted_reps:
            print(f"{RED}{name} : {reps}{RESET}")

def view_streak(data, dict_name):
    print("\n"+"="*60)
    print(f"{YELLOW}{'NAME':<15} | {'STREAK':<12}{RESET}")
    print("-"*60)
    print(f"{PURPLE}{dict_name:<15} | {data[dict_name]['Streak']:<12}{RESET}")
    
def calc_bmi(height, weight):
    print(f"{GREEN}Showing BMI{RESET}")
    bmi = round(weight/((height/100)**2), 2)
    print(f"{GREEN}Your BMI is {bmi}{RESET}")
    
#....................................MENU.............................................
def menu():
    print("\n1) Create profile")
    print("2) Add exercise")
    print("3) Add reps")
    print("4) Mark done")
    print("5) View profile")
    print("6) View streak")
    print("7) Calculate BMI")
    print("8) Exit")
    
    while True:
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            return choice
#.........................................MAIN.........................................
def main():
    data = load_data()
    while True:
        print(CYAN, end = "")
        user = menu()
        
        if user == "1":
            dict_name = input("Create profile name: ").strip().lower()
            if dict_name in data:
                print(f"{RED}This already exists{RESET}")
            else:
                bmi = input("Enter your BMI: ")
                create_profile(data, dict_name, bmi)
        elif user == "2":
            dict_name = input("Enter profile name: ").strip().lower()
            if dict_name not in data:
                print(f"{RED}No such profile{RESET}")
            else:
                exercise = input("Enter exercise name: ").strip().lower()
                if exercise in data[dict_name]["Exercises"]:
                    print(f"{RED}This exercise already exists{RESET}")
                else:
                    add_exercise(data, dict_name, exercise)
        elif user == "3":
            dict_name = input("Enter profile name: ").strip().lower()
            if dict_name not in data:
                print(f"{RED}No such profile{RESET}")
            else:
                exercise = input("Enter exercise name: ").strip().lower()
                if exercise not in data[dict_name]["Exercises"]:
                    print(f"{RED}No such exercise{RESET}")
                else:
                    try:
                        reps = int(input("Enter reps: "))
                        add_reps(data, dict_name, exercise, reps)
                    except:
                        print(f"{RED}Invalid reps{RESET}")
        elif user == "4":
            dict_name = input("Enter profile name: ").strip().lower()
            if dict_name not in data:
                print(f"{RED}No such profile{RESET}")
            else:
                if data[dict_name]["Last done"] == str(date.today()):
                    print(f"{RED}Streak already added{RESET}")
                else:
                    mark_done(data, dict_name)
                    data[dict_name]["Last done"] = str(date.today())
        elif user == "5":
            dict_name = input("Enter profile name: ").strip().lower()
            if dict_name not in data:
                print(f"{RED}No such profile{RESET}")
            else:
                view_profile(data, dict_name)
        elif user == "6":
            dict_name = input("Enter profile name: ").strip().lower()
            if dict_name not in data:
                print(f"{RED}No such profile{RESET}")
            else:
                view_streak(data, dict_name)
        elif user == "7":
            try:
                height = int(input("Enter your height in cm: "))
                weight = int(input("Enter your weight in kg: "))
                calc_bmi(height, weight)
            except:
                 print(f"{RED}An error occured{RESET}")
        elif user == "8":
            print("Bye")
            break
        save_data(data)
main()