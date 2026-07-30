"""
Project     : German Flashcards
Author      : Pleng
Day         : Day 25
Language    : Python

Concepts:
- Dictionary
- Functions
- while loop
- if / else
- .get()
- .items()
- .pop()

Features:
- Add new vocabulary
- Show all vocabulary
- Search German words
- Remove vocabulary
- Exit program

Description:
A simple German vocabulary flashcard application.
Users can add, search, display, and remove vocabulary
using a Python dictionary.
"""


## Header
def header():
    print("==========================================")
    print("            GERMAN FLASHCARDS             ")
    print("==========================================")


## Menu
def show_menu():
    list_menu = ["Add Word", "Show Words", "Search Word", "Remove Word", "Exit"]
    count = 1
    for menu in list_menu:
        print(f"{count}. {menu}")
        count += 1


## Add word
def add_word(words):
    german_word = input("German: ")
    if german_word in words:
        print("This word already exists.")
    else:
        english_word = input("English: ")
        words[german_word] = english_word
        print()
        print("Word added successfully.")

## Show words
def show_words(words):
    if len(words) == 0:
        print("No vocabulary yet.")
    else:
        print("German Vocabulary")
        print()
        for key, value in words.items():
            print(f"{key} - {value}")

## Search word
def search_word(words):
    if len(words) == 0:
        print("No vocabulary yet.")
    else:
        print("Search German word: ")
        word_to_search = input()
        print("Meaning:")
        print(words.get(word_to_search, "Word not found."))

## Remove word
def remove_word(words):
    if len(words) == 0:
        print("No vocabulary yet.")
    else:
        word_to_remove = input("German Word: ")
        if word_to_remove not in words:
            print("This word does not exist.")
        else:
            words.pop(word_to_remove)
            print()
            print("Word removed successfully.")


## Exit
def exit_text():
    print("Goodbye!")


## Run Code
words = {}

choice = 0

while choice != 5:
    header()
    print()
    show_menu()
    print()
    try:
        choice = int(input("Choose: "))
        if choice in [1, 2, 3, 4, 5]:
            print()
        else:
            print("Invalid input.")
            continue
    except:
        print("Invalid input. Please enter a number.")
        print()
        continue
    if choice == 1:
        add_word(words)
    elif choice == 2:
        show_words(words)
    elif choice == 3:
        search_word(words)
    elif choice == 4:
        remove_word(words)
    elif choice == 5:
        exit_text()
    print()
