# ============================================
#               Characters(GAME)
# ============================================

# ===================IMPORTS==================

import json
import os
import random
import sys

# ====================COLORS==================

CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"

# ===================CONFIG==================

FILE_PATH = "/storage/emulated/0/Python learning/things made by Siddharth/309th_quest_game.txt"

# ====================ENEMIES================

QUESTS = {
    "1": {"name": "Zombie", "exp": 20,  "attack": 20, "health": 50},
    "2": {"name": "Golem", "exp": 50,  "attack": 50 , "health": 175},
    "3": {"name": "Wither", "exp": 200,  "attack": 150, "health": 300},
    "4": {"name": "Ender dragon", "exp": 300, "attack": 200, "health": 450},
    "5": {"name": "Warden", "exp": 500, "attack": 350, "health": 550}
}

# ===============DATA HANDLING==============
class DataManager:
  """Data manager - Manages data from the file"""
 
  def __init__(self):
    self.file_path = FILE_PATH
  
  def load_data(self):
    if os.path.exists(self.file_path):
      try:
        with open(self.file_path, "r") as file:
          content = file.read()
          return json.loads(content) if content else {}
      except:
        return {}
    return {}
    
  def save_data(self, data):
    with open(self.file_path, "w") as file:
      json.dump(data, file, indent=4)
  
  

# ================PARENT CLASS==============

class Character:
  """Parrent class - Character"""
  def __init__(self, data_manager: DataManager, quest: str, name: str, exp: int = 0, level: int = 1, health: int = 100, attack: int = 20):
    self.data_manager = data_manager
    self.name = name
    self.quest = quest
    data = self.data_manager.load_data()
    
    if self.name in data:
      self.exp = data[self.name]["Exp"]
      self.level = data[self.name]["Level"]
      self.health = data[self.name]["Health"]
      self.attack = data[self.name]["Attack"]
      self.is_new = False
    else:
      self.exp = exp
      self.level = level
      self.health = health
      self.attack = attack
      self.is_new = True
    
  def save_character(self):
    data = self.data_manager.load_data()
    data[self.name] = {
      "Class": self.__class__.__name__,
      "Exp": self.exp, 
      "Level": self.level,
      "Health": self.health,
      "Attack": self.attack
    }
    self.data_manager.save_data(data)
  
  def display_info(self):
    data = self.data_manager.load_data()
    
    if self.name not in data:
      print(f"{RED}No such name{RESET}")
      return
    
    print(f"{YELLOW}\nName: {self.name}{RESET}")
    print(f"{YELLOW}Exp: {data[self.name]['Exp']}{RESET}")
    print(f"{YELLOW}Level: {data[self.name]['Level']}{RESET}")
    print(f"{YELLOW}Health: {data[self.name]['Health']}{RESET}")
    print(f"{YELLOW}Attack: {data[self.name]['Attack']}{RESET}")
    print(f"{GREEN}Note: On every 100 exp you level up and you health and attack increases by 5{RESET}")
  
  def quests(self):
    print("\n"+"="*60)
    print(f"{YELLOW}{'Enemy':<20} | {'Exp':<12} | {'Attack':<8} | {'Health':<4}{RESET}")
    print("-"*60)
    for quest in QUESTS:
      print(f"{PURPLE}{QUESTS[quest]['name']:<20} | {QUESTS[quest]['exp']:<12} | {QUESTS[quest]['attack']:<8} | {QUESTS[quest]['health']:<4}")
      
  def take_quest(self):
    self.quests = QUESTS
    
    data = self.data_manager.load_data()
    
    if self.name not in data:
      print(f"{RED}No such profile{RESET}")
      return
    
    print(f"{YELLOW}Your quest is to kill {self.quests[self.quest]['name']}{RESET}")
    
    player_potential = self.attack * self.health
    enemy_potential = self.quests[self.quest]["attack"] * self.quests[self.quest]["health"]
    
    
    
    if self.name in data and data[self.name]["Class"] == "Warrior":
      rage_choice = input(f"{PURPLE}Do you want to use the autonomous ultra rage mode?(Yes/No){RESET}: ").strip().lower()
      if rage_choice == "yes":
        player_potential = self.rage_mode()
    
    
    elif self.name in data and data[self.name]["Class"] == "Mage":
      spell_choice = input(f"{PURPLE}Do you want to caste the furious spells?(Yes/No){RESET}: ").strip().lower()
      if spell_choice == "yes":
        player_potential, enemy_potential = self.cast_spell()
        
    elif self.name in data and data[self.name]["Class"] == "Assassin":
      crit_choice = input(f"{PURPLE}Do you want to use the boundless gamble do shadow step?(Yes/No){RESET}: ").strip().lower()
      if crit_choice == "yes":
        player_potential = self.shadow_step()
    
    print(f"{GREEN}Your overall potential is {player_potential}\n Enemy's overall potential is {enemy_potential}")
    
    if player_potential < enemy_potential:
      print(f"{RED}Try again, You lost\nTip: Increase attack and health by killing slime{RESET}")
    
    elif player_potential == enemy_potential:
      print(f"{RED}Try again, It's a draw\nTip: Increase attack and health by killing slime{RESET}")
    
    elif player_potential > enemy_potential:
      print(f"{YELLOW}Good job, You defeated {self.quests[self.quest]['name']}")
      self.exp += self.quests[self.quest]["exp"]
      
      while self.exp >= 100:
        self.level += 1
        self.attack += 5
        self.health += 5
        self.exp -= 100
        self.save_character()
     
      self.save_character()

# =============CHILD CLASS 1==============

class Warrior(Character):
  """Child class - Warrior"""
  
  def __init__(self, data_manager:DataManager, quest: str, name: str, exp: int = 0, level: int = 1, health: int = 100, attack: int = 20):
    super().__init__(data_manager,quest, name, exp, level, health, attack)
    if self.is_new:
      self.attack += 20
      self.health += 20
      self.save_character()
    
  def rage_mode(self):
    print(f"{RED}Enteringggg.\nThe autonomous ultra rage modeeee!!!!{RESET}")
    health_loss = int((20/100)*self.health)
    sacrificed_hp = self.health - health_loss
    raged_atk = self.attack * 2
    
    self.raged_potential = sacrificed_hp * raged_atk
    print(f"{RED}{self.name} has entered the autonomous rage_mode and broke all the limits with his new potential {self.raged_potential}")
    return self.raged_potential
    
# ==============CHILD CLASS 2==============

class Mage(Character):
  """Child class- Mage"""
  def __init__(self, data_manager:DataManager, quest: str, name: str, exp: int = 0, level: int = 1, health: int = 100, attack: int = 20):
    super().__init__(data_manager,quest, name, exp, level, health, attack)
    
    if self.is_new:
      self.attack += 35
      self.save_character()
      
  def cast_spell(self):
    print(f"{RED}Casting the furious spells of the mage.Behold!{RESET}")
    enemy_drain = int((20/100)*
    QUESTS[self.quest]["health"])
    
    siphoned_player_hp = self.health + enemy_drain
    sucked_enemy_hp = QUESTS[self.quest]["health"] - enemy_drain
    
    rage_player_potential = siphoned_player_hp * self.attack
    sucked_enemy_potential = sucked_enemy_hp * QUESTS[self.quest]["attack"]
    return rage_player_potential, sucked_enemy_potential
  
class Assassin(Character):
  """Child class - Assassin"""
  
  def __init__(self, data_manager:DataManager, quest: str, name: str, exp: int = 0, level: int = 1, health: int = 100, attack: int = 20):
    super().__init__(data_manager,quest, name, exp, level, health, attack)
    
    if self.is_new:
      self.attack += 25
      self.save_character()
      
  def shadow_step(self):
    print(f"{RED}Using the boundless shadow_step gambling of Assassin{RESET}")
    crit_or_not = random.choice(["Crit", "Normal"])
    if crit_or_not == "Crit":
      crited_attack = self.attack * 3
      crit_potential = crited_attack * self.health
      return crit_potential
    else:
      normal_player_potential = self.attack * self.health 
      return normal_player_potential
      
# ==================MAIN PROGRAM=============
manager = DataManager()

print(f"{CYAN}====WELCOME TO QUEST GAME===={RESET}")

player_name = input(f"{CYAN}Please enter your name:{RESET}").strip().lower()

game_data = manager.load_data()

player = None

if player_name in game_data:
  saved_class = game_data[player_name]["Class"]
  
  print(f"Welcome back {player_name}! Loading your {saved_class} profile....{RESET}")
  
  Character.quests(None)
  while True:
    quest_choice = input(f"{CYAN}Enter the quest number you want to target{RESET}: ").strip()
    if quest_choice in ["1", "2", "3", "4", "5"]:
       break
  
  if saved_class == "Warrior":
    player = Warrior(manager, quest_choice, player_name)
  
  elif saved_class == "Mage":
    player = Mage(manager, quest_choice, player_name)
    
  elif saved_class == "Assassin":
    player = Assassin(manager, quest_choice, player_name)
    
else:
  print(f"{RED}Profile not found. Let's create a new character!{RESET}")
  
  player_name = input(f"{CYAN}Create a name:{RESET}").strip().lower()
  
  if player_name in game_data:
    print(f"{RED}This profile already exists{RESET}")
    sys.exit() # I wasnt able to add this but i had to bcz i cant use retun here as return can only be used in function and if i add else it will take me time
  
  print(f"{CYAN}Choose one of the characters bellow:{CYAN}")
  print(f"{YELLOW}NOTE- The default attack is 20 and the default hp is 100{RESET}")
  
  print(f"\n{PURPLE}1) Warrior\nBuffs- \nattack +20\nhealth +20\nSpecial move- The autonomous ultra rage(Sacrifice 20% hp and boost attack by 2){RESET}")
  
  print(f"{PURPLE}2) Mage\nBuffs- \nattack +35\nhealth +0\nSpecial move- The furious spells(sucks 20% opponets hp and adds to himself){RESET}")
  
  print(f"{PURPLE}3) Assassin\nBuffs- \nattack +25\nhealth +0\nSpecial move- The boundless shadow step gambling(50% chance of getting 3x attack boost){RESET}")
  while True:
    class_choice = input(f"{CYAN}Enter your choice(1-3):{RESET}").strip()
    if class_choice in ["1", "2", "3"]:
      break
  
  
  Character.quests(None)
  while True:
    quest_choice = input(f"{CYAN}Enter quest choice: {RESET}").strip()
    if quest_choice in ["1", "2", "3", "4", "5"]:
      break
    
  if class_choice == "1":
    player = Warrior(manager, quest_choice, player_name)
  elif class_choice == "2":
    player = Mage(manager, quest_choice, player_name)
  elif class_choice == "3":
    player = Assassin(manager, quest_choice, player_name)
  
if __name__ == "__main__":
  if player is not None:
    while True:
      print(CYAN, end = "")
      print("\n"+"="*60)
      print(f"==MAIN MENU==({player.__class__.__name__})")
      print("-"*60)
      
      print("\n1) Display character info")
      print("2) See all quests")
      print("3) Do quest(Battle)")
      print("4) Switch quest")
      print("5) Exit")
      
      choice = input("Select an option(1-5): ").strip()
      
      if choice == "1":
        player.display_info()
        
      elif choice == "2":
        player.quests()
        
      elif choice == "3":
        player.take_quest()
        
      elif choice == "4":
        print("\n"+"="*60)
        print("===Choose a new quest===")
        print("-"*60)
        Character.quests(None)
        new_quest = input("Enter new quest from above(1-5): ").strip()
        if new_quest in QUESTS:
          player.quest = new_quest
          print(f"{PURPLE}Target successfully switched to: {QUESTS[new_quest]['name']}!!!{RESET}")
        else:
          print(f"{RED}Please choose a valid quest{RESET}")
        
        
      elif choice == "5":
        print("Bye, Your progress is saved\nVisit again")
        break