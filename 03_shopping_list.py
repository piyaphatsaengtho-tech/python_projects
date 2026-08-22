"""
Project     : Shopping List & Budget Estimator
Author      : Pleng
Days        : 41 - 46
Language    : Python

Concepts Learned:

- Object-Oriented Programming (OOP)
- Classes
- Objects
- __init__()
- self
- Methods
- Dictionaries
- File Handling
- Pickle
- with open()
- Exception Handling
- Input Validation
- Data Persistence
- Refactoring

Features:

- Add shopping items
- Delete shopping items
- Edit item names
- Edit item prices
- Edit item quantities
- Mark items as bought or not bought
- Show shopping list
- Calculate estimated total price
- Set a shopping budget
- Compare total price with budget
- Show remaining money or over-budget amount
- Remember previously entered item prices
- Save shopping list data to file
- Load shopping list data from file
- Main Menu
- Edit Menu

Description:

A command-line shopping list and budget estimator application.

The program uses Object-Oriented Programming to manage shopping items,
calculate total costs, compare them with a budget, and track bought status.

Shopping list data and remembered item prices are saved using pickle
and automatically loaded when the program starts.

This project was built to practice OOP, input validation,
exception handling, file handling, and refactoring.
"""

import pickle

# Dictionary
price_memory = {}


# Class ShoppingItem
class ShoppingItem:
    def __init__(self, name, price, quantity, bought):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.bought = bought


# Functions
def show_shopping_list_label():
    print("             Let's Shop!            ")
    print("------------------------------------")

def get_price(name):
    name = name.strip().lower()
    if name in price_memory:
        return price_memory[name]
    
    while True:
        try:
            price = float(input("Estimated price: "))
            if price > 0:
                break
            print("Oh, the price must be greater than 0!")
        except ValueError:
            print("Oh, invalid input. Please enter the price again :)")

    price_memory[name] = price
    return price

def show_edit_menu():
    print("             Edit Menu             ")
    print()

    list_menu = ["Edit Name", "Edit Price", "Edit Quantity", "Back"]
    count = 1

    for menu in list_menu:
        print(f"{count}. {menu}")
        count += 1

def get_menu_choice(allowed_choices):
    while True:
        try:
            choice = int(input("Choose: "))
            if choice in allowed_choices:
                return choice
            print("Invalid input. Try again :-)")
            print()
        except ValueError:
            print("Oh, invalid input. Please enter a number :-)")
            print()

def show_main_menu():
    print("             Main Menu             ")
    print()

    list_menu = [
        "Add item",
        "Delete item",
        "Edit item",
        "Mark as bought",
        "Show my list",
        "Calculate total",
        "Budget",
        "Clear my list",
        "Exit"
    ]

    count = 1
    for menu in list_menu:
        print(f"{count}. {menu}")
        count += 1


# Class ShoppingList
class ShoppingList:
    def __init__(self):
        self.items = []
        self.budget = None

    def check_empty_shopping_list(self):
        if not self.items:
            print("We don't have anything yet :(")
            return False
        return True

    def get_item_from_user(self):
        name = input("Item name: ")

        for item in self.items:
            if name.strip().lower() == item.name.strip().lower():
                return item
            
        print("Item not found.")
        return None
    

    def add(self):
        while True:
            get_name = input("Item name: ")
            name = get_name.strip()
            if name == "":
                print("Invalid input. Please enter item name again ;)")
                continue
            break

        price = get_price(name)

        while True:
            try:
                quantity = int(input("Quantity: "))
                if quantity > 0:
                    break
                print("Oh, quantity must be greater than 0.")
            except ValueError:
                print("Oh, invalid input. Please enter a number :-)")
          
        item = ShoppingItem(name, price, quantity, False)
        self.items.append(item)
        print(f"{item.name} has been added successfully!")
        self.save()

    def delete(self):
        if not self.check_empty_shopping_list():
            return
        
        item = self.get_item_from_user()
        if item is None:
            return
        
        self.items.remove(item)
        print(f"{item.name} has been deleted successfully!")
        self.save()

    def edit(self):
        if not self.check_empty_shopping_list():
            return

        choice = 0
        while choice != 4:
            show_edit_menu()
            print()

            allowed_choices = [1,2,3,4]
            choice = get_menu_choice(allowed_choices)
            print()

            if choice == 1:
                self.edit_name()
                print()
            elif choice == 2:
                self.edit_price()
                print()
            elif choice == 3:
                self.edit_quantity()
                print()
            elif choice == 4:
                return

    def edit_name(self):
        item = self.get_item_from_user()
        if item is None:
            return

        old_name = item.name.strip().lower()

        while True:
            get_new_name = input("New item name: ")
            new_name = get_new_name.strip()
            if new_name == "":
                print("Invalid input. Please enter new item name again ;)")
                print()
                continue
            break

        price = price_memory[old_name]
        price_memory.pop(old_name, None)
        price_memory[new_name.lower()] = price

        item.name = new_name
        print()
        print("Name updated successfully.")
        self.save()

    def edit_price(self):
        item = self.get_item_from_user()
        if item is None:
            return

        while True:
            try:
                new_price = float(input("New price: "))
                if new_price > 0:
                    break
                print("Oh, the price must be greater than 0!")
            except ValueError:
                print("Oh, invalid input. Please enter the price again :)")

        price_memory[item.name.strip().lower()] = new_price
        item.price = new_price
        print()
        print("Price updated successfully.")
        self.save()

    def edit_quantity(self):
        item = self.get_item_from_user()
        if item is None:
            return

        while True:
            try:
                new_quantity = int(input("New quantity: "))
                if new_quantity > 0:
                    break
                print("Oh, quantity must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number ;)")

        item.quantity = new_quantity
        print()
        print("Quantity updated successfully.")
        self.save()

    def mark_as_bought(self):
        if not self.check_empty_shopping_list():
            return
        
        item = self.get_item_from_user()
        if item is None:
            return

        item.bought = not item.bought

        if item.bought:
            print(f"Yay, your {item.name} has already been bought.")
        else:
            print(f"Oh, {item.name} hasn't been bought yet.")

        self.save()

    def show_list(self):
        if not self.check_empty_shopping_list():
            return
        show_shopping_list_label()
        
        print("             Your List               ")
        print()

        for item in self.items:
            if not item.bought:
                bought_text = "No"
            else:
                bought_text = "Yes"

            print(
                f"Item name: {item.name}\n"
                f"Price: {item.price:.2f}\n"
                f"Quantity: {item.quantity}\n"
                f"Bought: {bought_text}"
            )
            print("____________________________________")
        print()

        total_price = self.calculate_total()
        if self.budget is None:
            print(f"Budget: Not set")
        else:
            print(f"Budget: {self.budget:.2f}")
            result = self.calculate_budget(total_price)
            self.show_budget(result)

    def calculate_total(self):
        total_price = 0
        for item in self.items:
            item_total = item.price * item.quantity
            print(f"{item.name}: {item_total:.2f}")
            total_price += item_total

        print("====================================")
        print(f"Total price: {total_price:.2f}")
        return total_price

    def clear_list(self):
        self.items = []
        print("Shopping list cleared successfully.")
        self.save()


    def get_budget(self):
        while True:
            get_answer_budget = input("Do you have a budget? (Yes/No): ")
            answer_budget = get_answer_budget.strip().lower()

            if answer_budget == "yes":
                while True:
                    try:
                        self.budget = float(input("Your budget: "))
                        if self.budget > 0:
                            return self.budget
                        print("Oh, the budget must be greater than 0!")
                    except ValueError:
                        print("Oh, invalid input. Please enter your budget again :)")
            elif answer_budget == "no":
                print("Okay, no budget set.")
                self.budget = None
                return self.budget
            print("Please enter only yes or no.")


    def calculate_budget(self, total_price):
        if self.budget is None:
            return

        result = self.budget - total_price
        return result

    def show_budget(self, result):
        if self.budget is None:
            return

        if result < 0:
            over_budget = result * -1
            print(f"Over budget: {over_budget:.2f}")
        elif result > 0:
            print(f"Money left: {result:.2f}")
        elif result == 0:
            print("Exactly on budget.")


    def save(self):
        with open("shopping_list.pkl", "wb") as file_shopping_list:
            pickle.dump(self.items, file_shopping_list)
        
        with open("price_memory.pkl", "wb") as file_price_memory:
            pickle.dump(price_memory, file_price_memory)

    def load(self):
        try:
            with open("shopping_list.pkl", "rb") as file_shopping_list:
                self.items = pickle.load(file_shopping_list)
        except FileNotFoundError:
            self.items = []

        try:
            with open("price_memory.pkl", "rb") as file_price_memory:
                load_price_memory = pickle.load(file_price_memory)

            normalize_price_memory = {}

            for name, price in load_price_memory.items():
                normalize_price_memory[name.strip().lower()] = price

            price_memory.clear()
            price_memory.update(normalize_price_memory)
        except FileNotFoundError:
            price_memory.clear()


# Full Program Flow
shopping_list = ShoppingList()

shopping_list.load()

choice = 0
while choice != 9:
    show_shopping_list_label()
    show_main_menu()
    print()  
    allowed_choices = [1,2,3,4,5,6,7,8,9]
    choice = get_menu_choice(allowed_choices)
    print()

    if choice == 1:
        shopping_list.add()
        print()
    elif choice == 2:
        shopping_list.delete()
        print()
    elif choice == 3:
        shopping_list.edit()
        print()
    elif choice == 4:
        shopping_list.mark_as_bought()
        print()
    elif choice == 5:
        shopping_list.show_list()
        print()
    elif choice == 6:
        shopping_list.calculate_total()
        print()
    elif choice == 7:
        shopping_list.get_budget()
        print()
    elif choice == 8:
        shopping_list.clear_list()
        print()
    elif choice == 9:
        print("Have a nice day :))")