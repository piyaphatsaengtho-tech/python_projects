# Project : User Profile
# Day : 20
# Author : Pleng
# Language : Python
# Concepts :
# - Functions
# - Parameters
# - Return
# - while loop
# - if / elif / else
# - try / except
# - continue
# - Input Validation
# - Update Data
# Description: A simple user profile that allows users to
# view and update their name and age through a menu.


def get_name():
  return input("Name: ")

name = get_name()

def change_name():
  return input("Enter new name: ")


def get_age():
  while True:
    try:
      return int(input("Age: "))
    except:
      print("Invalid age.")
      print()
      continue

age = get_age()

def change_age():
  while True:
    try:
      return int(input("Enter new age: "))
    except:
      print("Invalid age.")
      print()
      continue


def line():
  return "======================================="

def header_name():
  return "             USER PROFILE             "


def show_menu():
  list_menu = ["Show Name", "Show Age", "Check Adult",
               "Change Name", "Change Age", "Exit"]
  count = 1
  for menu in list_menu:
    print(count, menu)
    count += 1


def show_name(name):
  return "Your name is " + name + "."

def show_age(age):
  return f"You are {age} years old."

def check_adult(age):
  if age > 60:
    return "You are a senior."
  elif age >= 18:
    return "You are an adult."
  else:
    return "You are under 18."

def exit_message(name):
  return "Goodbye, " + name + "!"


print()
choice = 0
while choice != 6:
  print(line())
  print(header_name())
  print(line())
  print()
  show_menu()
  print()
  try:
    choice = int(input("Choose: "))
  except:
    print("Invalid input. Please enter a number.")
    print()
    continue
  if choice == 1:
    print(show_name(name))
  elif choice == 2:
    print(show_age(age))
  elif choice == 3:
    print(check_adult(age))
  elif choice == 4:
    name = change_name()
    print("Name updated successfully.")
  elif choice == 5:
    age = change_age()
    print("Age updated successfully.")
  elif choice == 6:
    print(exit_message(name))
  print()
