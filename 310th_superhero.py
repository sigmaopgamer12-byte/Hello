# ============================================
#                SUPERHERO GAME
# ============================================

# ===================IMPORTS==================

import os
import json
import random

# ===================COLORS===================

CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"

# =================CONFIG===================

FILE_PATH = "/storage/emulated/0/Python learning/things made by Siddharth/superhero_game.txt"

# ==============DATA MANAGER===============

class DataManager:
  """Handles all file operations"""

  def load(self):
    if os.path.exists(FILE_PATH):
      try:
        with open(FILE_PATH, "r") as file:
          content = file.read()
          return json.loads(content) if content else {}
      except:
        return {}
    return {}
    
  def save(self, data):
    with open(FILE_PATH, "w") as file:
      json.dump(data, file, indent=4)
      
# ==============PARENT CLASS================

class SuperHero():
  """Parent class - SuperHero"""
  
  def __init__(self, data_manager: DataManager, name: str, char_class: str):
    self.char_class = char_class
    self.data_manager = data_manager
    """Player datas"""
    
    self.name = name
    self.exp = 0
    self.level = 1
    self.health = 100
    self.attack = 20
    self.stamina = 100
    
    self.load_progress()
    
  def load_progress(self):
    data = self.data_manager.load()
    
    if self.name in data:
      self.exp= data[self.name].get("Exp", 0)
      self.level = data[self.name].get("Level", 1)
      self.health = data[self.name].get("Health", 100)
      self.attack = data[self.name].get("Attack", 20)
      self.stamina = data[self.name].get("Stamina", 100)
      print(f"{YELLOW}Welcome back, {self.name}!!!{RESET}")
      
    else:
      print(f"{YELLOW}Creating new character named {self.name}!!!{RESET}")
      
  def save_progress(self):
    data = self.data_manager.load()
    
    data[self.name] = {
      "Class": self.char_class,
      "Exp": self.exp,
      "Level": self.level,
      "Health": self.health,
      "Attack": self.attack,
      "Stamina": self.stamina
    }
    
    self.data_manager.save(data)
    
  def level_up(self):
    while self.exp >= 100:
      self.level += 1
      self.health += 5 
      self.attack += 5
      self.stamina += 5
      self.exp -= 100
      print(f"{PURPLE}Leveled up!! {self.name} is now level {self.level}!!!{RESET}")
    self.save_progress()
    
  def display_info(self):
    print(f"{YELLOW}==={self.name} the {self.char_class}==={RESET}")
    print(f"{PURPLE}\nName: {self.name}")
    print(f"\nClass: {self.char_class}")
    print(f"\nExp: {(self.exp)/100}")
    print(f"\nLevel: {self.level}")
    print(f"\nHealth: {self.health}")
    print(f"\nAttack: {self.attack}")
    print(f"\nStamina: {self.stamina}{RESET}")
    
# ==============CHILD CLASS 1=============
"""Child class - Speedster"""

class Speedster(SuperHero):
  def __init__(self, data_manager, name):
    super().__init__(data_manager, name, "Speedster")
    if self.level == 1 and self.exp == 0:
      self.attack += 20
      self.exp = 1
      self.save_progress()
      
  def time_rush(self):
    print(f"{RED}Activated flashiest time rush!!!{RESET}")
    sacrificed = int((30/100)* self.stamina)
    self.stamina -= sacrificed
    boosted = self.attack * 2
    print(f"{PURPLE}Sacrificed 30% stamina to get 2x attack!!!{RESET}")
    return self.stamina * boosted * self.health
    
# =============CHILD CLASS 2================
class Blaster(SuperHero):
  def __init__(self, data_manager, name):
    super().__init__(data_manager, name, "Blaster")
    if self.level == 1 and self.exp == 0:
      self.attack += 30
      self.exp = 1
      self.save_progress()
      
  def overcharge_blast(self):
    print(f"{RED}Activated gamble of overcharge blast!!!{RESET} ")
    death_alive = random.choice(["Death", "Alive", "Death"])
    if death_alive == "Death":
      print(f"{RED}Your blast killed you{RESET}")
      return 0
    else:
      boosted = self.attack * 4
      print(f"{PURPLE}Won the gamble and got 3x attack boost!!{RESET}")
      return boosted * self.health * self.stamina
      
# ===============CHILD CLASS 3=================

class Tank(SuperHero):
  """Child class - Tank"""
  
  def __init__(self, data_manager, name):
    super().__init__(data_manager, name, "Tank")
    
    if self.level == 1 and self.exp ==0:
      self.health += 20
      self.stamina += 15
      self.exp = 1
      self.save_progress()
      
  def iron_defense(self):
    print(f"{RED}Activating the ultimate iron defense!!{RESET}")
    sacrificed = int((50/100)* self.attack)
    self.attack -= sacrificed
    boosted = self.health * 3
    print(f"{RED}Activated the ultimate iron defense for 50% attack and boosted health by 3x!!{RESET}")
    return self.attack * self.stamina * boosted
    
# ================CHILD CLASS 4================

class Shadow(SuperHero):
  """Child class - Shadow"""
  
  def __init__(self, data_manager, name):
    super().__init__(data_manager, name, "Shadow")
    
    if self.level == 1 and self.exp == 0:
      self.attack +=20
      self.stamina += 15
      self.exp = 1
      self.save_progress()
      
  def shadow_assult(self):
    print(f"{RED}Activating the furious crit gamble of Shadow!!!{RESET}")
    crit_choice = random.choice(["Crit", "Normal"])
    if crit_choice == "Crit":
      boosted = self.attack *2
      print(f"{RED}Crit landed the attack boosted by 2!!!{RESET}")
      return boosted * self.health * self.stamina
      
    else:
      print(f"{RED}Crit failed no boosts!!{RESET}")
      return self.attack * self.health * self.stamina
      
# ===================ENEMIES=================
ENEMIES = {
    "1": {"name": "King Kong", "exp": 20, "attack": 30, "health": 100, "stamina": 100},
    "2": {"name": "Godzilla", "exp": 50, "attack": 80, "health": 100, "stamina": 100},
    "3": {"name": "Cake queen", "exp": 200, "attack": 100, "health": 150, "stamina": 100},
    "4": {"name": "Dough king", "exp": 300, "attack": 150, "health": 200, "stamina": 200},
    "5": {"name": "Indra", "exp": 500, "attack": 250, "health": 400, "stamina": 300}
}

# ================MAIN GAME==================
if __name__ == "__main__":
  print(CYAN, end = "")
  
  manager = DataManager()
  
  print("=====SuperHero - GAME=====\n")
  
  name = input("Enter your character name: ").strip().lower()
  
  data = manager.load()
  
  if name in data:
    saved_class = data[name]["Class"]
    
    if saved_class == "Speedster":
      player = Speedster(manager, name)
    
    elif saved_class == "Blaster":
      player = Blaster(manager, name)
    
    elif saved_class == "Tank":
      player = Tank(manager, name)
      
    else:
      player = Shadow(manager, name)
    
  else:
    print(f"{GREEN}Creating new character {name}!!{RESET}")
    
    print("\n====CHOOSE YOUR CLASS====")
    
    print(f"{YELLOW}NOTE- The default attack is 20,  the default hp is 100 and default stamina is 100{RESET}")
    
    print(f"\n{PURPLE}1) Speedster\nBuffs- \nattack +20\nhealth +0\nstamina +0\nSpecial move- The flashiest time rush(Sacrifice 30% stamina and boost attack by 2x){RESET}")
    
    print(f"{GREEN}2) Blaster\nBuffs- \nattack +30\nhealth +0\nstamina + 0\nSpecial move- The gamble of overcharge blash(has 75% of dying with his own blast if alive he gets attack boost by 4x){RESET}")
    
    print(f"{RED}3) Tank\nBuffs- \nattack +0\nhealth +20\nstamina + 15\nSpecial move- The ultimate iron defense(lose 50% attack and get 3x health){RESET}")
    
    print(f"{YELLOW}4) Shadow\nBuffs- \nattack +20\nhealth +0\nstamina + 15\nSpecial move- The furious crit gamble of Shadow(has 50% chance of crit if crit attack boosted by 2x){RESET}")
    while True:
      choice = input("Ented choice(1-4): ").strip()
      if choice in ["1", "2", "3", "4"]:
        break
    
    if choice == "1":
      player = Speedster(manager, name)
    
    elif choice == "2":
      player = Blaster(manager, name)
    
    elif choice == "3":
      player = Tank(manager, name)
      
    else:
      player = Shadow(manager, name)
      
  print(f"{GREEN}WELCOME, {player.name} the {player.char_class}!{RESET}")
  
  while True:
    
    print(f"{PURPLE}=====MENU====={RESET}")
    
    print(CYAN, end = "")
    
    print("\n1) Display info")
    print("2) Fight enemy")
    print("3) Exit")
    
    menu_choice = input("Enter your choice(1-3): ").strip()
    
    if menu_choice == "1":
      player.display_info()
    
    elif menu_choice == "2":
      print("\nAvailable enemies:")
      
      for title, info in ENEMIES.items():
        print(f"{PURPLE}{title}>> {info['name']} (Exp:{info['exp']}){RESET}")
        
      enemy_choice = input("Enter enemy number: ").strip()
      
      if enemy_choice in ENEMIES:
        enemy = ENEMIES[enemy_choice]
        print(f"{RED}Fighting enemy: {enemy['name']}{RESET}")
        
        potential = player.attack * player.health * player.stamina
        
        enemy_potential = enemy["attack"] * enemy["health"] * enemy["stamina"]
        
        ultimate_choice = input(f"{RED}Do you want to use ultimate?(Yes/No): {RESET}").strip().lower()
        
        if ultimate_choice == "yes":
          if isinstance(player, Speedster):
            potential = player.time_rush()
          
          elif isinstance(player, Blaster):
            potential = player.overcharge_blast()
          
          elif isinstance(player, Tank):
            potential = player.iron_defense()
          
          else:
            potential = player.shadow_assult()
            
        if potential > enemy_potential:
          print(f"{GREEN}Victory! +{enemy['exp']} EXP{RESET}")
          player.exp += enemy["exp"]
          player.level_up()
          
        else:
          print(f"{RED}You were defeated...Train harder!!{RESET}")
    elif menu_choice == "3":
      print(f"{YELLOW}See you next time..{player.name} the {player.char_class}!{RESET}")
      break