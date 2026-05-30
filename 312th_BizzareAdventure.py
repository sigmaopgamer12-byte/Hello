# ================================================
#               ELEMENTAL WARRIORS
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
FILE_PATH = "/storage/emulated/0/Python learning/things made by Siddharth/CastSpell.txt"

ENEMIES: Dict[str, Dict[str, Any]] = {
  "1": {
    "name": "Jonathem",
    "exp": 30,
    "attack": 20,
    "health": 100,
    "stamina": 120
  },
  
  "2": {
    "name": "Jojuro",
    "exp": 50,
    "attack": 60,
    "health": 115,
    "stamina": 130
  },
  
  "3": {
    "name": "Joseph",
    "exp": 100,
    "attack": 160,
    "health": 160,
    "stamina": 130
  }
}

# ==================DATA MANAGER=================

class DataManager:
  """DataManager - Manages data"""
  
  def __init__(self, file_path: str = FILE_PATH):
    self.file_path = file_path
    
  def load(self) -> Dict[str, Any]:
    """Load - loads data from the file"""
    
    if os.path.exists(self.file_path):
      try:
        with open(self.file_path, "r") as file:
          content = file.read()
          return json.loads(content) if content else {}
      except:
        return {}
    return {}
    
  def save(self,  data: Dict[str, Any]) -> None:
    """Save - saves data"""
    
    with open(self.file_path, "w", encoding = "utf-8") as file:
      json.dump(data, file, indent=4)
      
# =================PARENT CLASS=================

class Character:
  """Parent class - CastSpell"""
  
  def __init__(self, data_manager: DataManager, name: str, char_class: str):
    """main values"""
    self.data_manager = data_manager
    self.name = name
    self.char_class = char_class
    
    """default values"""
    
    self.exp = 0
    self.level = 1
    self.attack = 20
    self.mana = 100
    self.health = 100
    
    self.load_data()
  
  def load_data(self):
    """load_data - loads data for furthur use"""
    
    data = self.data_manager.load()
    
    if self.name in data:
      player_data = data[self.name]
      
      self.char_class = player_data.get("class", "None")
      self.exp = player_data.get("exp", 0)
      self.level = player_data.get("level", 1)
      self.attack = player_data.get("attack", 20)
      self.mana = player_data.get("mana", 100)
      self.health = player_data.get("health", 100)
      # new or old check
      self.is_new = False
      
    else:
      self.is_new = True
      
  def save_data(self):
    """save_data - saves player's data"""
    
    data = self.data_manager.load()
    
    data[self.name] = {
      "exp": self.exp,
      "class": self.char_class,
      "level": self.level,
      "attack": self.attack,
      "mana": self.mana,
      "health": self.health
    }
    
    self.data_manager.save(data)
    
  def show_profile(self):
    """show_profile - shows users profile"""
    
    print("\n" + "=" * 60)
    print(f"{YELLOW}==={self.name} the {self.char_class}==={RESET}")
    print("\n" + "¢" * 60)
    print(f"{PURPLE}Name: {self.name.title()}")
    print(f"Class: {self.char_class}")
    print(f"Exp: {self.exp}")
    print(f"Level: {self.level}")
    print(f"Attack: {self.attack}")
    print(f"Mana: {self.mana}")
    print(f"Health: {self.health}{RESET}")
    
    print("\n" + "-" * 30)
    
  def level_up(self):
    """level_up - works on level up logic"""
    while self.exp >= 100:
      self.exp -= 100
      self.level += 1
      self.attack += 5
      self.mana += 5 
      self.health += 5
      print(f"{YELLOW}Player {self.name} has leveled up to {self.level}{RESET}")
    
    self.save_data()
    
  def base_power(self) -> int:
    """calculates base combat potential"""
    
    return self.attack * self.mana * self.health
    
  def calculate_power(self, use_ultimate: bool = False) -> int:
    """Calculate power and overwrite it in child class"""
    
    return self.base_power()
    
  def enemy_power(self, choice: str) -> int:
    """Calculates enemy power"""
    enemy = ENEMIES[choice]
    return enemy["attack"] * enemy["stamina"] * enemy["health"]
    
# ==============CHILD CLASS 1==================

class Dio(Character):
  """child class 1 - Dio"""
  
  def __init__(self, data_manager: DataManager, name: str):
    super().__init__(data_manager, name, "Dio")
    
    if self.is_new:
      self.attack += 20
      self.mana += 10
      self.save_data()
      
  def calculate_power(self, use_ultimate: bool = False) -> int:
    
    if not use_ultimate:
      return self.base_power()
      
    boosted = self.attack * 2
    lost = (15/100)*self.health
    sacrificed = self.health - lost
    
    print(f"{RED}Dio mask mode on!!!{RESET}")
    return int(boosted * sacrificed * self.mana)
    
# =================CHILD CLASS 3==============

class Karls(Character):
  """child class 2 - Karls"""
  
  def __init__(self, data_manager: DataManager, name: str):
    super().__init__(data_manager, name, "Karls")
    
    if self.is_new:
      self.health += 30
      self.attack -= 6
      self.save_data()
      
  def calculate_power(self, use_ultimate: bool = False) -> int:
    
    if not use_ultimate:
      return self.base_power()
      
    lost = (25/100) * self.mana
    sacrificed = self.mana - lost
    boosted = self.health * 1.5
    
    print(f"{RED}Karls the immortal!!{RESET}")
    
    return int(boosted * sacrificed * self.attack)
    
# ==============CHILD CLASS 4================

class Yamcha(Character):
  """child class 3 - Yamcha"""
  
  def __init__(self, data_manager: DataManager, name: str):
    super().__init__(data_manager, name, "Yamcha")
    
    if self.is_new:
      self.attack += 10
      self.health += 10
      self.mana += 10
      self.save_data()
      
  def calculate_power(self, use_ultimate: bool = False) -> int:
    
    if not use_ultimate:
      return self.base_power()
      
    lost = (25/100) * self.mana
    sacrificed = self.mana - lost
    boosted = self.attack * 3
    
    print(f"{RED}Yamcha pose!!{RESET}")
    
    return int(sacrificed * boosted * self.health)
    
# ==============CHARACTER FACTORY=============

def create_character(data_manager: DataManager, username: str, choice: str) -> Character:
  """create_character - return created character"""
  
  character_class = {
    "1": Dio,
    "2": Karls,
    "3": Yamcha
  }
  
  return character_class[choice](data_manager, username)
  
def load_character(data_manager: DataManager, username: str):
  """load_character - loads existing character"""
  
  data = data_manager.load()
  
  character_class = data[username]["class"]
  
  character_map = {
    "Dio": Dio,
    "Karls": Karls,
    "Yamcha": Yamcha
  }
  
  return character_map[character_class](data_manager, username)
  
def fight(player) -> None:
  """handles fight"""
  print("\n" + "=" * 60)
  print(f"{PURPLE}===AVAILABLE ENEMIES==={RESET}")
  print("\n" + "=" * 60)
  
  for key, opponent in ENEMIES.items():
    power = opponent["attack"] * opponent["health"] * opponent["stamina"]
    print(f"{YELLOW}==={opponent['name']}==={RESET}")
    print(f"{PURPLE} {key}. Exp: {opponent['exp']} | Power: {power:6}{RESET}")
    
  choice = input(f"{GREEN}Enter your choice(1-3): {RESET}").strip()
    
  if choice not in ENEMIES:
    print(f"{RED}Invalid choice{RESET}")
    return
  
  use_ult_input = input(f"{RED}Want to use ultimate(yes/no): {RESET}").strip().lower()
  use_ultimate = use_ult_input in ("yes", "y")
  
  player_potential = player.calculate_power(use_ultimate)
  
  opponent = ENEMIES[choice]
  
  enemy_potential = player.enemy_power(choice)
  
  print("\n" + "-" * 30)
  print(f"{YELLOW}===CLASH==={RESET}")
  print("\n" + "-" * 30)
  
  print(f"{PURPLE} Your power: {player_potential}")
  print(f"Enemy potential: {enemy_potential}{RESET}")
  
  if player_potential > enemy_potential:
    print(f"{GREEN}You defeated {opponent['name']} {RESET}")
    player.exp += opponent['exp']
    print(f"{GREEN}+{opponent['exp']} exp{RESET}")
    player.level_up()
      
  else:
    print(f"{RED}You lost in battle with {opponent['name']}{RESET}")
      
# ==================MAIN======================

def main() -> None:
  """Main program"""
  
  print(CYAN, end = "")
  
  data_manager = DataManager()
  data = data_manager.load()
  
  username = input("Enter your username: ").strip().lower()
  
  if not username:
    print(f"{RED}Username cant be empty{RESET}")
    return 
    
  if username in data:
    print(f"{YELLOW}Welcome back!! {username} the {data[username]['class']}{RESET}")
    player = load_character(data_manager, username)
    
  else:
    print(f"{GREEN}Creating new character named {username}{RESET}")
    print(f"{YELLOW}Choose one of the charcters below:{RESET}")
    print(f"{PURPLE}\n1) Dio")
    print("2) Karls")
    print(f"3) Yamcha{RESET}")
    
    while True:
      choice = input(f"{YELLOW}Enter your choice (1-3): {RESET}").strip()
      
      if choice in ["1", "2", "3"]:
        player = create_character(data_manager, username, choice)
        print(f"{GREEN}Welcome!! {username} the {player.char_class}{RESET}")
        break
      
      else:
        print(f"{RED}Invalid choice{RESET}")
        
  # =================GAME LOOP================
  
  while True:
    print("\n" + "=" * 60)
    print(f"{YELLOW}===MENU==={RESET}")
    print("\n" + "=" * 60)
    
    print(CYAN, end = "")
    
    print(f"{PURPLE}Choose one of the options below: {RESET}")
    print(f"{YELLOW}\n1) Show info")
    print("2) Fight enemy")
    print(f"3) Exit{RESET}")
    
    menu_choice = input(f"{GREEN}Enter your choice(1-3): {RESET}").strip()
    
    if menu_choice == "1":
      player.show_profile()
      
    elif menu_choice == "2":
      fight(player)
      
    elif menu_choice == "3":
      player.save_data()
      print(f"{GREEN}Bye....{RESET}")
      break
    
    else:
      print(f"{RED}Invalid choice{RESET}")
      
# ===================EXECUTION==============

if __name__ == "__main__":
  
  #try:
   main()
   """ 
  except KeyboardInterrupt:
    print("\nGame terminated by user")
    
  except Exception as e:
    print(f"{RED}An unexpected error occured {e}{RESET}")"""