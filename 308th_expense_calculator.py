# ==========================================
#             EXPENSE CALCULATOR
# ==========================================

# ==================IMPORTS=================

import os 
import json
from datetime import date

# ==================COLORS=================

CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"
RESET = "\033[0m"

# ==================CONFIG=================

FILE_PATH = "/storage/emulated/0/Python learning/things made by Siddharth/expense_calculator.txt"

# ==================CLASS==================

class expense_calculator:
  # ==============DATA HANDLING==============
  def __init__(self):
    self.data = self.load_data()
  
  def load_data(self):
    """Load data from json file"""
    if os.path.exists(FILE_PATH):
      try:
        with open(FILE_PATH,"r") as file:
          content = file.read()
          return json.loads(content) if content else {}
      except:
        return {}
    return {}
    
  def save_data(self):
    with open(FILE_PATH, "w") as file:
      json.dump(self.data, file, indent=4)
      
  # ==============CORE FEATURES==============
  
  # ======Create profile======
  
  def add_expense(self, name: str, amount: int, category: str, description: str ):
    if name in self.data:
      return False
    
    print(f"{GREEN}Creating your expense{RESET}")
    self.data[name] = {
      "Amount": amount,
      "Category": category,
      "Description": description,
      "Date": date.today().isoformat()
    }
    self.save_data()
    print(f"{GREEN}EXPENSE successfully created for {name}! {RESET}")
    return True
    
  # =======View expense today========
  
  def today_expense(self):
    
    today = date.today().isoformat()
    total_sum = 0
    for name, info in self.data.items():
      if info["Date"] == today:
        total_sum += info["Amount"]
    if total_sum == 0:
      return False
    else:
      print(f"{GREEN}Your total expense for today is {total_sum}! {RESET}")
      return True
    
  # =======monthly spent=======
  
  def monthly_expense(self, month: str):
    
    amount = 0
    
    exact_month = f"-{month}-"
    
    for name, info in self.data.items():
      if exact_month in info["Date"]:
        amount += info["Amount"]
    if amount == 0:
        return False
    else:
        print(f"{GREEN}Your total expense of {month} is {amount}! {RESET}")
        return True
    
  # ========expense by category=======
  def expense_category(self, category: str):
    expense_list = []
    for name, info in self.data.items():
      if info["Category"] == category:
        expense_list.append(name)
    if not expense_list:
      return False
    print(f"{GREEN}Expeses of category {category} are listed below\n{expense_list}! {RESET}")
    return True
    
  # =======Delete expense======
  def delete_expense(self, name: str):
    if name not in self.data:
      return False
    del self.data[name]
    print(f"{GREEN} {name} successfully deleted! {RESET}")
    self.save_data()
    return True
# ==================MAIN===================
if __name__ == "__main__":
  calculator = expense_calculator()
  print(f"{PURPLE}=======WELCOME TO EXPENSE LISTER======{RESET}")
  
  while True:
    print(CYAN, end = "")
    print("\n1) Create expense")
    print("2) Calculate today expense")
    print("3) Calculate monthly expense")
    print("4) Find expense by category")
    print("5) Delete expense")
    print("6) Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
      name = input("Enter expense name: ")
      amount_str = input("Enter expense amount: ")
      category = input("Enter expense category: ")
      description = input("Enter expense description")
      try:
        amount = int(amount_str)
      except:
        print(f"{RED}Please enter a valid amount{RESET}")
        continue
      success = calculator.add_expense(name, amount, category, description)
      if not success:
        print(f"{RED}This expense already exists! {RESET}")
    
    elif choice == "2":
      print(f"{GREEN}Showing today expense...{RESET}")
      success =  calculator.today_expense()
      if not success:
        print(f"{RED} No expense listed on today's date!{RESET}")
    
    elif choice == "3":
      month = input("Enter the month of which expense you want: ")
      print(f"{GREEN} Showing the amount....{RESET}")
      success = calculator.monthly_expense(month)
      if not success:
          print(f"{RED}No expenses on the given month{RESET}")
    
    elif choice == "4":
      category = input("Enter category of which expense you want: ")
      success = calculator.expense_category(category)
      if not success:
        print(f"{RED} No expense with category {category}! {RESET}")
    
    elif choice == "5":
      name = input("Enter expense name: ")
      success = calculator.delete_expense(name)
      if not success:
        print(f"{RED} No expense named {name}! {RESET}")
    
    elif choice == "6":
      print(f"{YELLOW}Thanks!!! See you again {RESET}")
      break