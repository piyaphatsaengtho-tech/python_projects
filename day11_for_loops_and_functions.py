# ========================================
# Topic: For Loops and Functions Practice
# Day: 11
# Author: Pleng
# Description: This file contains practice exercises for:
# - for loops
# - range()
# - functions
# - functions with parameters
# ========================================

# ========================================
# For Loops
# ========================================

fruits = ["Apple", "Banana", "Orange", "Mango"]
for fruit in fruits:
  print("I like", fruit)
print()

numbers = [3, 7, 10, 15]
for number in numbers:
  print(number * 2)
print()

animals = ["Cat", "Dog", "Rabbit"]
for animal in animals:
  print("Animal:")
  print(animal)
  print()

print("===== Shopping List =====")
print()

shopping_list = ["Milk", "Bread", "Egg", "Apple"]
count = 1

for item in shopping_list:
  print(count, item)
  count = count + 1
print()

print("Total:", len(shopping_list), "items")
print()

for greet in range(5):
  print("Hello")
print()

for i in range(2, 11, 2):
  print(i)
print()

for i in range(10, 4, -1):
  print(i)
print()

for i in range(1, 6):
  print(i ** 2)
print()

# ===================================
# Functions
# ===================================
def say_name():
  print("My name is Pleng.")
say_name()
say_name()
say_name()
print()

def line():
  print("===============")
line()
print("Shopping List")
line()
print()

def show_menu():
  menu = ["Add", "Remove", "Show", "Exit"]
  count = 1
  for item in menu:
    print(count, item)
    count = count + 1
print()
print("Menu")
show_menu()
print()
print("Menu Again")
show_menu()
print()

def greet(name):
  print("Hello,", name + "!")
greet("Pleng")
greet("Pot")
greet("Phing")
print()

def square(number):
  print(number ** 2)
square(2)
square(5)
square(10)
print()

def greet_with_age(name, age):
  print("Hello,", name + "!", "You are", age, "years old.")
greet_with_age("Pleng", 23)
print()

def rectangle(width, height):
  print("Width:", width)
  print("Height:", height)
rectangle(5, 10)
print()

def cube(number):
  print(number ** 3)
cube(3)
print()

def introduce(name, country):
  print("Hello! My name is", name + ".")
  print("I come from", country + ".")
introduce("Pleng", "Thailand")
print()
