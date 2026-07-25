"""
Project    : Todo List
Author     : Pleng
Day        : Day 21
Language   : Python

Concepts:
- Lists
- Functions
- Parameters
- Return
- for loop
- while loop
- if / elif / else
- try / except
- continue
- Input Validation

Description:
A simple Todo List that allows users to:
- Add tasks
- Show tasks
- Remove tasks
- Exit the program
"""

def line():
  return "=============================="

def header_name():
  return "           TODO LIST          "

def show_todo_list():
  todo_list = ["Add Task", "Show Tasks", "Remove Task",
               "Exit"]
  count = 1
  for todo in todo_list:
    print(count, todo)
    count+= 1


tasks =[]


def add_task(tasks):
  new_task = input("Enter Task: ")
  return tasks.append(new_task)

def show_tasks(tasks):
  count = 1
  print("Your Tasks:")
  for task in tasks:
    print(count, task)
    count += 1

def remove_task(tasks):
  while True:
    try:
      remove_number = int(input("Enter task number to remove: "))
      return tasks.remove(tasks[remove_number - 1])
    except:
      print("Invalid input. Please try again")
      continue


def exit_message():
  return "Goodbye!"


choice = 0

while choice != 4:
  print(line())
  print(header_name())
  print(line())
  print()
  show_todo_list()
  print()
  try:
    choice = int(input("Choose: "))
    print()
  except:
    print("Invalid input. Please enter a number.")
    print()
    continue
  if choice == 1:
    add_task(tasks)
    print()
    print("Task added successfully.")
  elif choice == 2:
    if len(tasks) == 0:
      print("No task yet.")
    else:
      show_tasks(tasks)
  elif choice == 3:
    if len(tasks) == 0:
      print("No task yet")
    else:
      show_tasks(tasks)
      print()
      remove_task(tasks)
      print()
      print("Task removed successfully.")
  elif choice == 4:
    print(exit_message())
  print()