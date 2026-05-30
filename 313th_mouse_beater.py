# ================================================
#                 MOUSE BEATER
# ================================================

# ====================IMPORTS=====================

import json
import os
from typing import Dict, Any, Optional

# ====================COLORS=====================

CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"

# ====================CONFIG====================
FILE_PATH = "/storage/emulated/0/Python learning/things made by Siddharth/MouseBeater.txt"

ENEMIES: Dict[str, Dict[str, Any]] = {
  "1": {
    "name": "Pawn mouse",
    "exp": 30,
    "attack": 20,
    "health": 100,
    "energy": 120,
    "drop": 5 
  },
  
  "2": {
    "name": "Boss mouse",
    "exp": 50,
    "attack": 60,
    "health": 115,
    "energy": 130,
    "drop": 10
  },
  
  "3": {
    "name": "Micky mouse",
    "exp": 100,
    "attack": 160,
    "health": 160,
    "energy": 130,
    "drop": 15
  }
}

FOODS: Dict[str, Dict[str, Any]] = {
  "samosha": {
    "attack": 2,
    "health": 5,
    "energy": 5,
    "cost": 15
  },
  
  "momo": {
    "attack": 5,
    "health": 8,
    "energy": 7,
    "cost": 30
  },
  
  "pizza": {
    "attack": 8,
    "health": 12,
    "energy": 12,
    "cost": 50
  }
}
# ==================DATA MANAGER=================

class DataManager:
  """DataManager - manages all the datas"""
  
  def __init__(self, file_path: str = FILE_PATH):
    self.file_path = file_path
    
  def load(self):
    """load - loads player data from the file"""
    if os.path.exists(FILE_PATH):
      try:
        with open(FILE_PATH, "r") as file:
          content = file.read()
          return json.loads(content) if content else {}
      except:
        return {}
    return {}
    
  def save(self, data: Dict[str, Any]) -> None:
    """save - saves player's data"""
    
    with open(FILE_PATH, "w", encoding = "utf-8") as file:
      json.dump(data, file, indent=4)
      
# ==================PARENT CLASS==================
class Pet:
  """Pet - Parent class"""
  
  def __init__(self, data_manager: DataManager, name:str, pet_class: str):
    # main values
    self.data_manager = DataManager()
    self.name = name
    self.pet_class = pet_class
    
    # default values
    self.happiness = 0
    self.level = 1
    self.attack = 20
    self.health = 100
    self.energy = 100
    self.balance = 0
    self.foods = []
    
    self.load_data()
    
  def load_data(self):
    """load_data - loads player data and checks if the name exists or not"""
    
    data = self.data_manager.load()
    
    if self.name in data:
      player_data = data[self.name]
      
      self.pet_class = player_data.get("pet_class", "None")
      self.happiness = player_data.get("happiness", 0)
      self.level = player_data.get("level", 1)
      self.attack = player_data.get("attack", 20)
      self.health = player_data.get("health", 100)
      self.energy = player_data.get("energy", 100)
      self.balance = player_data.get("balance", 0)
      self.foods = player_data.get("foods", [])
      # new or old check
      self.is_new = False
    
    else:
      self.is_new = True
      
  def save_data(self):
    data = self.data_manager.load()
    
    data[self.name] = {
      "pet_class": self.pet_class,
      "happiness": self.happiness,
      "level": self.level,
      "attack": self.attack,
      "health": self.health,
      "energy": self.energy,
      "balance": self.balance,
      "foods": self.foods
    }
    
    self.data_manager.save(data)
    
  def show_info(self):
    """show_info - shows player info"""
    print("\n" + "=" * 60)
    print(f"{YELLOW}==={self.name}'s {self.pet_class}==={RESET}")
    print("\n" + "$" * 60)
    
    print(f"{PURPLE}Name: {self.name.title()}")
    print(f"Pet: {self.pet_class}")
    print(f"Happiness: {self.happiness}")
    print(f"Level: {self.level}")
    print(f"Attack: {self.attack}")
    print(f"Health: {self.health}")
    print(f"Energy: {self.energy}")
    print(f"Foods: {self.foods}")
    print(f"Balance: {self.balance}{RESET}")
    
    print("\n" + "-" * 30)
    
  def level_up(self):
    """level_up - works on level up logic"""
    
    while self.happiness >= 100:
      self.level += 1
      self.attack += 5
      self.health += 5
      self.energy += 5
      self.happiness -= 100
      
      print(f"{GREEN}Congrats!! You leveled up to {self.level}{RESET}")
    self.save_data()
    
  def base_power(self) -> int:
    """calculates base power"""
    
    return self.attack * self.health * self.energy
    
  def calculate_potential(self, use_ultimate: bool = False) -> int:
    """calculates potential and overwrite it in child class"""
    
    return self.base_power()
    
  def enemy_power(self, choice: str) -> int:
    """gives enemy's power"""
    
    enemy = ENEMIES[choice]
    
    return enemy["attack"] * enemy["health"] * enemy["energy"]
    
  def food_system(self, food_choice: str) -> int:
    try:
      noname = FOODS[food_choice]
      
      return int(noname["attack"] * noname["health"] * noname["energy"])
      
    except:
      return 0

# =================CHILD CLASS 1================

class Kitsune(Pet):
  """Child class 1 - Kitsune"""
  
  def __init__(self, data_manager: DataManager, name: str):
    super().__init__(data_manager, name, "Kitsune")
    
    if self.is_new:
      self.attack += 15
      self.energy += 20
      self.save_data()
      
  def calculate_potential(self, use_ultimate: bool = False) -> int:
    
    if not use_ultimate:
      return self.base_power()
      
    lost = (20/100) * self.health
    sacrificed = self.health - lost
    boosted = self.attack * 2 
    
    print(f"{RED}Kitsune fire!!{RESET}")
    return int(sacrificed * boosted * self.energy)
    
# ================CHILD CLASS 3===================

class Phoenix(Pet):
  """child class 2 - Phoenix"""
  
  def __init__(self, data_manager: DataManager, name: str):
    super().__init__(data_manager, name, "Phoenix")
    
    if self.is_new:
      self.attack -= 15
      self.health += 30
      self.save_data()
      
  def calculate_potential(self, use_ultimate: bool = False) -> int:
    
    if not use_ultimate:
      return self.base_power()
      
    lost = (50/100) * self.attack
    sacrificed = self.attack - lost
    boosted = self.health * 2
    
    print(f"{RED}Phoenix defense!!{RESET}")
    return int(sacrificed * boosted * self.energy)
    
# =================CHILD CLASS 3================

class Dragon(Pet):
  """child class 3 - Dragon"""
  
  def __init__(self, data_manager: DataManager, name: str):
    super().__init__(data_manager, name, "Dragon")
    
    if self.is_new:
      self.attack += 30
      self.energy -= 5
      self.save_data()
      
  def calculate_potential(self, use_ultimate: bool = False) -> int:
    
    if not use_ultimate:
      return self.base_power()
      
    lost = (30/100) * self.energy
    sacrificed = self.energy - lost
    boosted = self.attack * 3
    
    print(f"{RED}Dragon burst!!{RESET}")
    return int(sacrificed * boosted * self.health)
    
# ================CHARACTER FACTORY==============

def create_character(data_manager: DataManager, username: str, choice: str) -> Pet:
  """create_character - returns created character"""
  
  character_class = {
    "1": Kitsune,
    "2": Phoenix,
    "3": Dragon
  }
  
  return character_class[choice](data_manager, username)
  
def load_character(data_manager, username) -> Pet:
  """load_character - returns stored character"""
  
  data = data_manager.load()
  
  character_class = data[username]["pet_class"]
  
  character_map = {
    "Kitsune": Kitsune,
    "Phoenix": Phoenix,
    "Dragon": Dragon
  }
  
  return character_map[character_class](data_manager, username)
  
def fight(player) -> None:
  """handles fight"""
  
  print("\n" + "=" * 60)
  print(f"{YELLOW}===AVAILABLE ENEMIES==={RESET}")
  print("\n" + "=" * 60)
  
  for key, opponent in ENEMIES.items():
    power = opponent["attack"] * opponent["health"] * opponent["energy"]
    
    print(f"{YELLOW}==={opponent['name']}==={RESET}")
    
    print(f"{PURPLE} {key}. Exp: {opponent['exp']} | Power: {power: 6} {RESET}")
    
  choice = input(f"{GREEN}Enter your choice(1-3): {RESET}").strip()
  
  if choice not in ENEMIES:
    print(f"{RED}Invalid choice{RESET}")
    return
    
  use_ult_input = input(f"{RED}Wanna use ultimate: {RESET}").strip().lower()
  
  use_ultimate = use_ult_input in ("yes", "y")
  
  player_potential = player.calculate_potential(use_ultimate)
  
  opponent = ENEMIES[choice]
  
  enemy_potential = player.enemy_power(choice)
  
  if not player.foods:
    print(f"{RED}No food to eat{RESET}")
    food_choice = 0
  
  else:
    print(f"{YELLOW}===AVAILABLE FOODS==={RESET}")
    print(f"{PURPLE}0. Dont eat")
    
    for seeds in player.foods:
      print(f"Food: {seeds}{RESET}")
      
    while True: 
      food_choice = input(f"{GREEN}Enter your choice: {RESET}").strip().lower()
      if food_choice in player.foods or food_choice == "0":
        
        try:
            player.foods.remove(food_choice)
        
        except:
            pass
        
        player.save_data()
        break
    
  food_potential = player.food_system(food_choice)
  
  player_potential += food_potential
  
  print("\n" + "-" * 30)
  print(f"{YELLOW}===CLASH==={RESET}")
  print("\n" + "-" * 30)
  
  print(f"{PURPLE}Your potential: {player_potential}")
  print(f"Enemy's potential: {enemy_potential}{RESET}")
  
  if player_potential > enemy_potential:
    print(f"{GREEN}You defeated {opponent['name']}{RESET}")
    player.happiness += opponent["exp"]
    player.balance += opponent["drop"]
    print(f"{GREEN}+{opponent['exp']} happiness {RESET}")
    print(f"{GREEN}+{opponent['drop']} to balance {RESET}")
    player.level_up()
    
  else:
    print(f"{RED}You lost in battle with {opponent['name']}{RESET}")
    
def buy_food(player) -> None:
  """handles buy food feature"""
  
  print("\n" + "=" * 60)
  
  print(f"{YELLOW}===AVAILABLE FOODS==={RESET}")
  
  for something, anything in FOODS.items():
    print(f"{PURPLE}==={something}==={RESET}")
    print(f"{YELLOW}=BOOSTS=")
    print(f"Atk: {anything['attack']} | Hp: {anything['health']} | En: {anything['energy']}{RESET}")
    print(f"{GREEN}Cost: {anything['cost']}{RESET}")
    
  print(f"{PURPLE}Your balance is: {player.balance}{RESET}")
  
  while True:
    buy_choice = input(f"{YELLOW}Enter fruit name which you want to buy: {RESET}").strip().lower()
    if buy_choice in FOODS:
      
      if player.balance >= FOODS[buy_choice]["cost"]:
        
        print(f"{GREEN}Food sucessfully bought{RESET}")
        
        player.foods.append(buy_choice)
        
        player.save_data()
        
        break
      
      else:
        print(f"{RED}Not enough balance{RESET}")
        break
    
    else:
      print(f"{RED}No such fruit{RESET}")
      
# =====================MAIN==================

def Main() -> None:
  """Main program"""
  data_manager = DataManager()
  data = data_manager.load()
  
  print(CYAN, end = "")
  
  username = input("Enter your username: ").strip().lower()
  
  if not username:
    print(f"{RED}Username cant be empty{RESET}")
    
  if username in data:
    print(f"{YELLOW}Welcome back!!!, {username} the {data[username]['pet_class']}{RESET}")
    player = load_character(data_manager, username)
    
  else:
    print(f"{YELLOW}Creating new character named {username}{RESET}")
    print(f"{GREEN}Choose one of the pet below: {RESET}")
    print(f"{PURPLE}1) Kitsune")
    print("2) Phoenix")
    print(f"3) Dragon")
    
    while True:
      choice = input(f"{GREEN}Enter your choice: {RESET}").strip()
      
      if choice in ["1", "2", "3"]:
        player = create_character(data_manager, username, choice)
        print(f"{GREEN}Welcome!!!{username} the {player.pet_class}{RESET}")
        break
      else:
        print(f"{RED}Invalid choice{RESET}")
        
  # ==================GAME LOOP================
  
  while True:
    print("\n" + "=" * 60)
    print(f"{YELLOW}===MENU==={RESET}")
    print("\n" + "=" * 60)
    
    print(f"{PURPLE}Choose one of the options below{RESET}")
    print(f"{YELLOW}1) Show info")
    print("2) Buy food")
    print("3) Fight enemy")
    print(f"4) Exit{RESET}")
    
    menu_choice = input(f"{GREEN}Enter your choice(1-3): {RESET}").strip()
    
    if menu_choice == "1":
      player.show_info()
    
    elif menu_choice == "2":
      buy_food(player)
      
    elif menu_choice == "3":
      fight(player)
      
    elif menu_choice == "4":
      player.save_data()
      print(f"{GREEN}Bye!! cya again{RESET}")
      break
    
    else:
      print(f"{RED}Invalid choice{RESET}")
  
# ==================EXECUTION===============

if __name__ == "__main__":
  
  Main()