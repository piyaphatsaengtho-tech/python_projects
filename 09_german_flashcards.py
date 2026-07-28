"""
Project    : German Flashcards
Author     : Pleng
Day        : Day 24
Language   : Python

Concepts:
- Dictionary
- Functions
- Parameters
- for loop
- while loop
- if / elif / else
- try / except
- Input Validation
- Dictionary Methods (.get(), .items())

Description:
A simple German Flashcards program that allows users to:
- Add German vocabulary with English meanings
- Show all saved vocabulary
- Search for a German word
- Prevent duplicate words
- Exit the program
"""


## Header
def header():
    print("==========================================")
    print("            GERMAN FLASHCARDS             ")
    print("==========================================")


## Menu
def show_menu():
    list_menu = ["Add Word", "Show Words", "Search Word", "Exit"]
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
        print("No vocabulary yet")
    else:
        print("German Vocabulary")
        print()
        for key, value in words.items():
            print(f"{key} - {value}")

## Search word
def search_word(words):
    if len(words) == 0:
        print("No vocabulary yet")
    else:
        print("Search German word: ")
        word_to_search = input()
        if word_to_search in words:
            print("Meaning:")
            print(words.get(word_to_search))
        else:
            print("Word not found.")

## Exit
def exit_text():
    print("Goodbye!")


## Run Code
words = {}

choice = 0

while choice != 4:
    header()
    print()
    show_menu()
    print()
    try:
        choice = int(input("Choose: "))
        if choice in [1, 2, 3, 4]:
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
        exit_text()
    print()