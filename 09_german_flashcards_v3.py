"""
Project     : German Flashcards
Author      : Pleng
Day         : Day 27
Language    : Python

New Concepts:
- Early Return
- Refactoring

New Features:
- Update vocabulary
- Refactored duplicated code
- Added check_dict_empty()

Description:
Refactored the project by introducing helper functions
and early return to improve readability.
"""


## Header
def header():
    print("==========================================")
    print("            GERMAN FLASHCARDS             ")
    print("==========================================")


## Menu
def show_menu():
    list_menu = ["Add Word", "Show Words", "Search Word", "Update Word", 
                 "Remove Word", "Exit"]
    count = 1
    for menu in list_menu:
        print(f"{count}. {menu}")
        count += 1


## Add word
def add_word(words):
    german_word = input("German: ")
    if german_word in words:
        print("This word already exists.")
        return
    
    english_word = input("English: ")
    words[german_word] = english_word
    print()
    print("Word added successfully.")

## Check dict empty
def check_dict_empty(words):
    return len(words) == 0

## Show words
def show_words(words):
    if check_dict_empty(words):
        print("No vocabulary yet.")
        return
    
    print("German Vocabulary")
    print()
    for key, value in words.items():
        print(f"{key} - {value}")

## Search word
def search_word(words):
    if check_dict_empty(words):
        print("No vocabulary yet.")
        return

    word_to_search = input("Search German word: ")
    print(f"Meaning: {words.get(word_to_search, 'Word not found.')}")

## Update word
def update_word(words):
    if check_dict_empty(words):
        print("No vocabulary yet.")
        return

    word_to_update = input("German: ")
    if word_to_update not in words:
        print("This word does not exist.")
        return
    
    print(f"Current meaning: {words[word_to_update]}")
    print()
    words[word_to_update] = input("New English: ")
    print()
    print("Word updated successfully.")

## Remove word
def remove_word(words):
    if check_dict_empty(words):
        print("No vocabulary yet.")
        return
    
    word_to_remove = input("German Word: ")
    if word_to_remove not in words:
        print("This word does not exist.")
        return
    
    words.pop(word_to_remove)
    print()
    print("Word removed successfully.")


## Exit
def exit_text():
    print("Goodbye!")


## Run Code
words = {}

choice = 0

while choice != 6:
    header()
    print()
    show_menu()
    print()
    try:
        choice = int(input("Choose: "))
        if choice in [1, 2, 3, 4, 5, 6]:
            print()
        else:
            print("Invalid input.")
            print()
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
        update_word(words)
    elif choice == 5:
        remove_word(words)
    elif choice == 6:
        exit_text()
    print()