"""
Project     : German Flashcards
Author      : Pleng
Day         : 35
Language    : Python

Concepts Learned:

- Functions
- Dictionary
- List
- Loops
- Methods
- Random Module
- File Handling
- Early Return
- Refactoring
- Error Handling
- Function Return Values

Features:

- Add vocabulary
- Show vocabulary
- Search vocabulary
- Update vocabulary
- Remove vocabulary
- Quiz: German -> English
- Quiz: English -> German
- Quiz: Mixed Mode
- Score System
- Save vocabulary to file
- Load vocabulary from file

Description:

A command-line flashcard application for learning German vocabulary.
Users can add, search, update, remove, and quiz German vocabulary.
The program supports three quiz modes and calculates the user's score.
Vocabulary data is stored in a text file so it is available every time
the program starts.
"""

import random

## Header
def header():
    print("==========================================")
    print("            GERMAN FLASHCARDS             ")
    print("==========================================")

## Menu
def show_menu():
    list_menu = ["Add Word", "Show Words", "Search Word",
                 "Update Word", "Remove Word", "Quiz", "Exit"]
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
    if word_to_search in words:
        print(f"Meaning: {words[word_to_search]}")
    else:
        print("Word not found.")

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


## Quiz
def quiz(words):
    if check_dict_empty(words):
        print("No vocabulary yet.")
        return

    while True:
        show_quiz_menu()
        print()
        choice = get_quiz_choice()
        print()

        if choice == 1:
            selected_words = prepare_question(words)
            score_count = DE_to_EN_questions(selected_words)
        elif choice == 2:
            selected_words = prepare_question(words)
            score_count = EN_to_DE_questions(selected_words)
        elif choice == 3:
            selected_words = prepare_question(words)
            score_count = mixed_questions(selected_words)
        elif choice == 4:
            return

        print(f"Your score is {score_count}/{len(selected_words)}.")
        print()


def show_quiz_menu():
    print("======= QUIZ MENU =======")
    print()
    quiz_menu = ["German -> English", "English -> German", "Mixed", "Back"]
    count = 1
    for menu in quiz_menu:
        print(f"{count}. {menu}")
        count += 1

def get_quiz_choice():
    while True:
        try:
            choice = int(input("Choose: "))
            if choice not in [1, 2, 3, 4]:
                print("Invalid input.")
                print()
            else:
                return choice
        except:
            print("Invalid input. Please enter a number 1 to 4.")
            print()
            continue

def get_question_count(words):
    print(f"You have {len(words)} words.")
    print()
    while True:
        try:
            count_question = int(input("How many questions would you like?: "))
            if count_question < 1 or count_question > len(words):
                print(f"You have only {len(words)} words. Please enter a number again.")
                print()
            else:
                return count_question
        except:
            print("Invalid input. Please enter a number.")
            continue

def prepare_question(words):
    count_question = get_question_count(words)
    print()
    selected_words = random_words(words, count_question)
    return selected_words

def random_words(words, count_question):
    words_list = list(words.items())
    selected_words = random.sample(words_list, count_question)
    return selected_words


def DE_to_EN_questions(selected_words):
    score_count = 0
    for german, english in selected_words:
        wrong_count = 0
        while wrong_count < 3:
            print(f"German: {german}")
            answer = input("English: ")
            print()
            if answer == english:
                print("Correct! Well done!")
                print()
                break
            elif wrong_count == 2:
                wrong_count += 1
            else:
                print("Almost! Try again!")
                print()
                wrong_count += 1

        if wrong_count == 3:
            print("Nice try!")
            print(f"The answer is: {english}")
        elif wrong_count < 3:
            score_count += 1
        print()

    return score_count

def EN_to_DE_questions(selected_words):
    score_count = 0
    for german, english in selected_words:
        wrong_count = 0
        while wrong_count < 3:
            print(f"English: {english}")
            answer = input("German: ")
            print()
            if answer == german:
                print("Correct! Well done!")
                print()
                break
            elif wrong_count == 2:
                wrong_count += 1
            else:
                print("Almost! Try again!")
                print()
                wrong_count += 1

        if wrong_count == 3:
            print("Nice try!")
            print(f"The answer is: {german}")
        elif wrong_count < 3:
            score_count += 1
        print()

    return score_count

def mixed_questions(selected_words):
    score_count = 0
    questions_list = ["DE_to_EN", "EN_to_DE"]
    for german, english in selected_words:
        selected_question = random.choice(questions_list)
        if selected_question == questions_list[0]:
            question = german
            correct_answer = english
            question_label = "German"
            answer_label = "English"
        else:
            question = english
            correct_answer = german
            question_label = "English"
            answer_label = "German"

        wrong_count = 0
        while wrong_count < 3:
            print(f"{question_label}: {question}")
            answer = input(f"{answer_label}: ")
            print()
            if answer == correct_answer:
                print("Correct! Well done!")
                break
            elif wrong_count == 2:
                wrong_count += 1
            else:
                print("Almost! Try again!")
                print()
                wrong_count += 1

        if wrong_count == 3:
            print("Nice try!")
            print(f"The answer is: {correct_answer}")
        elif wrong_count < 3:
            score_count += 1
        print()

    return score_count


## Exit
def exit_text():
    print("Goodbye!")


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

## Save words
def save_words(words):
    file = open("vocabulary.txt", "w")
    for key, value in words.items():
        file.write(f"{key}:{value}\n")
    file.close()

## Run Code
words = load_words()

choice = 0

while choice != 7:
    header()
    print()
    show_menu()
    print()
    try:
        choice = int(input("Choose: "))
        if choice in [1, 2, 3, 4, 5, 6, 7]:
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
        quiz(words)
    elif choice == 7:
        exit_text()
    print()
