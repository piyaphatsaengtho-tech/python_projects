"""
Project     : German Flashcards
Author      : Pleng
Day         : Day 31
Language    : Python

Concepts Learned:
- Functions
- Dictionary
- Loops
- File Handling
- Early Return
- Refactoring

Features:
- Add vocabulary
- Show vocabulary
- Search vocabulary
- Update vocabulary
- Remove vocabulary
- Save vocabulary to file
- Load vocabulary from file

Description:
A command-line flashcard application for learning German vocabulary.
Users can add, search, update, remove, and save vocabulary.
Data is stored in a text file so it is available every time the program starts.
"""


## Header
def header():
    print("==========================================")
    print("            GERMAN FLASHCARDS             ")
    print("==========================================")


## Menu
def show_menu():
    list_menu = ["Add Word", "Show Words", "Search Word", 
                 "Update Word", "Remove Word", "Exit"]
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


## Save words
def save_words(words):
    file = open("vocabulary.txt", "w")
    for key, value in words.items():
        file.write(f"{key}:{value}\n")
    file.close()

## Load words
def load_words():
    words = {}
    try:
        file = open("vocabulary.txt", "r") 
        for line in file:
            parts = line.strip().split(":")
            words[parts[0]] = parts[1]
        file.close()
        return words
    except:
        file = open("vocabulary.txt", "w")
        file.close()
        return words


## Run Code
words = load_words()

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
        save_words(words)
    elif choice == 2:
        show_words(words)
    elif choice == 3:
        search_word(words)
    elif choice == 4:
        update_word(words)
        save_words(words)
    elif choice == 5:
        remove_word(words)
        save_words(words)
    elif choice == 6:
        exit_text()
    print()