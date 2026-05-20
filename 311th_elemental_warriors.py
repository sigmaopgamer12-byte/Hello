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
FILE_PATH = "/storage/emulated/0/Python learning/things made by Siddharth/elemental_characters.txt"

ENEMIES: Dict[str, Dict[str, Any]] = {
  "1": {
    "name": "Goblin",
    "exp": 30,
    "attack": 20,
    "health": 100,
    "stamina": 120
  },
  
  "2": {
    "name": "Orc",
    "exp": 50,
    "attack": 60,
    "health": 115,
    "stamina": 130
  },
  
  "3": {
    "name": "Demon wolf",
    "exp": 100,
    "attack": 160,
    "health": 160,
    "stamina": 130
  }
}

# ==================DATA MANAGER=================
class DataManager():
  """DataManager - Manages data"""
  
  def __init__(self, file_path: str = FILE_PATH):
    self.file_path = file_path
    
  def load(self) -> Dict[str, Any]:
    """load- Loads all player data from the file"""
    
    if os.path.exists(self.file_path):
      try:
        with open(self.file_path, "r") as file:
          content = file.read()
          return json.loads(content) if content else {}
      except:
        return {}
    return {}
    
  def save(self, data: Dict[str, Any]) -> None:
    """save - saves all datas"""
    
    with open(self.file_path, "w", encoding = "utf-8") as file:
      json.dump(data, file, indent=4)

# ================PARENT CLASS================°
class Warrior:
  """Warrior - parent class(base class)"""
  
  def __init__(self, data_manager: DataManager, name: str, char_class: str):
    
    self.data_manager = data_manager
    self.name = name
    self.char_class = char_class
    
    # Default stats
    
    self.exp = 0
    self.level = 1
    self.attack = 20
    self.health = 100
    self.stamina = 100
    
    self.load_data()
    
  def load_data(self):
    """load_data - loads stored player data if available"""
    
    data = self.data_manager.load()
    
    if self.name in data:
      player_data = data[self.name]
      
      self.char_class = player_data.get("Class", "Empty")
      self.exp = player_data.get("exp", 0)
      self.level = player_data.get("level", 1)
      self.attack = player_data.get("attack", 20)
      self.health = player_data.get("health", 100)
      self.stamina = player_data.get("stamina", 100)
      self.is_new = False
      
    else:
      self.is_new = True
      
  def save_data(self):
    """save_data - saves user data"""
    data = self.data_manager.load()
    data[self.name] = {
      "Class": self.char_class,
      "exp": self.exp,
      "level": self.level,
      "attack": self.attack,
      "health": self.health,
      "stamina": self.stamina
    }
    self.data_manager.save(data)
    
  def show_profile(self) -> None:
    """Display players statistics"""
    
    print("\n" + "=" * 60)
    print(f"{YELLOW}==={self.name} the {self.char_class}===")
    print("\n" + "=" * 60)
    
    print(f"{PURPLE}Name: {self.name.title()}")
    print(f"Exp: {self.exp}")
    print(f"Level: {self.level}")
    print(f"Attack: {self.attack}")
    print(f"Health: {self.health}")
    print(f"Stamina: {self.stamina}{RESET}")
    
    print("\n" + "=" *60)
    
  def level_up(self) -> None:
    
    while self.exp >= 100:
      """level_up - handles level up logics"""
      self.exp -= 100
      self.level += 1
      self.attack += 5
      self.health += 10
      self.stamina += 10
      print(f"{YELLOW}Leveled up!! Level: {self.level}")
      
    self.save_data()
    
  def base_power(self) -> int:
    """Calculates base combat potential"""
    
    return self.attack * self.health * self.stamina
    
  def calculate_potential(self, use_ultimate: bool = False) -> int:
    """Calculate combat power and overwrite it in child class"""
    
    return self.base_power()
    
# ==================CHILD CLASS 1=================

class Flame(Warrior):
  """Child class 1 - Flame warrior"""
  
  def __init__(self, data_manager: DataManager, name: str):
    super().__init__(data_manager, name, "Flame")
    
    if self.is_new:
      self.stamina -= 10
      self.attack += 25
      self.save_data()
      
  def calculate_potential(self, use_ultimate: bool = False) -> int:
    if not use_ultimate:
      return self.base_power()
      
    self.stamina -= 30
    boosted = self.attack * 2
    print(f"{RED}Flame slash activated!{RESET}")
    return int(self.stamina * boosted * self.health)
    
# =================CHILD CLASS 2===============

class Thunder(Warrior):
  """Child calss 2 - Thunder warrior"""
  
  def __init__(self, data_manager: DataManager, name: str):
    super().__init__(data_manager, name, "Thunder")
    if self.is_new:
      self.stamina += 10
      self.attack += 15 
      self.save_data()
      
  def calculate_potential(self, use_ultimate: bool = False) -> int:
    if not use_ultimate:
      return self.base_power()
      
    loss = (20/100) * self.health 
    sacrificed = self.health - loss
    boosted_atk = self.attack * 1.50
    boosted_sta = self.stamina * 1.25
    print(f"{RED}Lightning strike activated!{RESET}")
    return int(sacrificed * boosted_sta * boosted_atk)
    
# ===============CHILD CLASS 3===============

class Ice(Warrior):
  """Child class 3 - Ice warrior"""
  
  def __init__(self, data_manager: DataManager, name: str):
    super().__init__(data_manager, name, "Ice")
    
    if self.is_new:
      self.attack -= 10
      self.health += 15
      self.stamina += 5 
      self.save_data()
      
  def calculate_potential(self, use_ultimate: bool = False) -> int:
    if not use_ultimate:
      return self.base_power()
      
    loss = (30/100) * self.attack
    sacrificed = self.attack - loss
    boosted_hp = self.health * 1.25
    boosted_stamina = self.stamina * 2
    print(f"{RED}Freezed shield activated!{RESET}")
    return int(sacrificed * boosted_stamina * boosted_hp)
    
# ================WARRIOR FACTORY==============

def create_character(data_manager: DataManager, username: str, choice: str) -> Warrior:
  """Factroy fucntion to create warrior instances"""
  
  character_classes = {
    "1": Flame,
    "2": Thunder,
    "3": Ice
  }
  return character_classes[choice](data_manager, username)
  
def load_existing_character(data_manager: DataManager, username: str) -> Warrior:
  """Factory function to laod existing warrior"""
  
  data = data_manager.load()
  
  character_class = data[username]["Class"]
  
  character_map = {
    "Flame": Flame,
    "Thunder": Thunder,
    "Ice": Ice
  }
  return character_map[character_class](data_manager, username)
  
def fight(player: Warrior) -> None:
  """Handles fights"""
  print("\n" + "=" * 60)
  print(f"{RED}===Available enemies==={RESET}")
  print("\n" + "=" * 60)
  
  for key, enemy in ENEMIES.items():
    power = enemy["attack"] * enemy["health"] * enemy["stamina"]
    print(f"{YELLOW}==={enemy['name']}==={RESET}")
    print(f"{PURPLE} {key}. Exp: {enemy['exp']} | Power: {power:6}{RESET}")
     
  choice = input("Enter your choice: ").strip()
     
  if choice not in ENEMIES:
    print(f"{RED}Invalid enemy choice{RESET}")
    return
     
  enemy = ENEMIES[choice]
     
  use_ult_input = input(f"{RED}Use ult(Yes/No): ").strip().lower()
  use_ultimate = use_ult_input in ("yes", "y")
     
  player_power = player.calculate_potential(use_ultimate)
  enemy_power = enemy["health"] * enemy["attack"] * enemy["stamina"]
     
  print("\n" + "=" * 60)
  print(f"{YELLOW}===Clash==={RESET}")
  print("\n" + "=" * 60)
     
  print(f"{YELLOW} Your power: {player_power}")
  print(f"Enemy power: {enemy_power}{RESET}")
     
  if player_power > enemy_power:
    print(f"{GREEN}You won {enemy['name']} defeated!{RESET}")
    player.exp += enemy['exp']
    print(f"{YELLOW} + {enemy['exp']} exp")
    player.level_up()
       
  else:
    print(f"{RED} You were defeated by {enemy['name']}{RESET}")
        
# ====================MAIN=====================

def main() -> None:
  """Main game program"""
  print(CYAN, end = "")
  
  data_manager = DataManager()
  data = data_manager.load()
  
  username = input("Enter your username: ").strip().lower()
  
  if not username:
    print(f"{RED}Username cant be empty{RESET}")
    return
  
  if username in data:
    print(f"{GREEN}Welcome back {username} the {data[username]['Class']}!!{RESET}")
    player = load_existing_character(data_manager, username)
    
  else:
    print(f"{GREEN}Creating new warrior {username}!!{RESET}")
    print(f"\n{YELLOW}Select one of the warrior{RESET}")
    print(f"{PURPLE}\n1) Flame")
    print("2) Thunder")
    print(f"3) Ice{RESET}")
    
    
    while True:
      choice = input(f"{YELLOW}Enter your choice(1-3): {RESET}").strip()
      if choice in ["1", "2", "3"]:
          player = create_character(data_manager, username, choice)
          print(f"{GREEN}Welcome! {player.name.title()} the {player.char_class} to arena{RESET}")
          break
          
      else:
          print(f"{RED}Invalid please enter (1-3): {RESET}")
  
  # ================GAME LOOP================
  while True:
    print("\n" + "=" * 60)
    print(f"\n{YELLOW}===MENU==={RESET}")
    print("\n" + "=" * 60)
    
    print(CYAN, end = "")
    
    print("Choose one of the options bellow:")
    print("\n1) Show info")
    print("2) Fight enemy")
    print("3) Save and exit")
    
    menu_choice = input(f"{PURPLE}Enter choice (1-3): {RESET}").strip()
    
    if menu_choice == "1":
      player.show_profile()
      
    elif menu_choice == "2":
      fight(player)
      
    elif menu_choice == "3":
      player.save_data()
      print(f"{YELLOW}Progress saved\nBye, {player.name.title()} the {player.char_class}")
      break
    
    else:
      print(f"{RED}Please enter your choice (1-3)")
      
# ===================EXECUTION===============

if __name__ == "__main__":
  """try:"""
  main()
    
  """except KeyboardInterrupt:
    print("\nGame terminated by user")
    
  except Exception as e:
    print(f"An unexpected error occured: {e}")"""