# ====================================
# Project: Shopping List
# Vertion: 2
# Day: 12
# Author: Pleng
# Description: A shopping list program using:
# - while loop
# - if-elif-else
# - list
# - functions
# - input
# Features:
# - Add items
# - Remove items
# - Show shopping list
# - Exit program
# ====================================

print("===== Shopping List =====")
print()
shopping_list = []
choose = 0

def show_menu():
  menu = ["Add items", "Remove item", "Show items", "Exit"]
  count = 1
  for item in menu:
    print(count, item)
    count = count + 1

def add_item():
  item = input("Add: ")
  shopping_list.append(item)

def remove_item():
  if len(shopping_list) == 0:
    print("We don't have anything yet :(")
  else:
    item = input("Remove: ")
    if item not in shopping_list:
      print("It is not in your list!")
    else:
      shopping_list.remove(item)

def show_items():
  if len(shopping_list) == 0:
    print("Shopping List is empty.")
  else:
    print("===== Shopping List =====")
    print()
    count = 1
    for item in shopping_list:
      print(count, item)
      count = count + 1
    print()
    print("Total:", len(shopping_list), "items")

while choose != 4:
  show_menu()
  print()
  choose = int(input("Choose: "))

  if choose == 1:
    add_item()
  elif choose == 2:
    remove_item()
  elif choose == 3:
    show_items()
  elif choose > 4 or choose <1:
    print("Please enter your correct choose!")
  else:
    print("Have a nice day!")
  print()
