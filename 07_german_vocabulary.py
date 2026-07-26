"""
Project    : German Vocabulary
Author     : Pleng
Day        : Day 22
Language   : Python

Concepts:
- Lists
- Functions
- Parameters
- for loop
- while loop
- if / else
- try / except
- Membership operator (in)
- Input Validation

Description:
A simple German Vocabulary program that allows users to:
- Add new words
- Show all words
- Search for a word
- Exit the program
"""

def line():
    return "======================================"

def header_name():
    return "           GERMAN VOCABULARY          "

def show_menu():
    list_menu = ["Add Word", "Show Words", "Search Word", "Exit"]
    count = 1
    for menu in list_menu:
        print(count, menu)
        count += 1

words = []

def add_word(words):
    new_word = input("Enter German word: ") 
    words.append(new_word)

def show_words(words):
    print("German Vocabulary:")
    count = 1
    for word in words:
        print(count, word)
        count += 1   

def search_word(words):
    word_to_search = input("Enter word: ")
    print()
    if word_to_search in words:
        print("Word found!")
    else:
        print("Word not found.")

def exit_message():
    return "Goodbye!"

choice = 0

while choice != 4:
    print(line())
    print(header_name())
    print(line())
    print()
    show_menu()
    print()
    try:
        choice = int(input("Choose: "))
        print()
    except:
        print("Invalid input. Please enter a number.")
        print()
        continue
    if choice == 1:
        add_word(words)
        print()
        print("Word added successfully.")
    elif choice == 2:
        if len(words) == 0:
            print("No word yet.")
        else:
            show_words(words)
    elif choice == 3:
        if len(words) == 0:
            print("No words yet.")
        else:
            search_word(words)
    elif choice == 4:
        print(exit_message())
    print()