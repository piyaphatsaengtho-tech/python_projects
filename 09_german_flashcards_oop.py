"""
Project     : German Flashcards
Author      : Pleng
Day         : 37
Language    : Python

Concepts Learned:

- Object-Oriented Programming (OOP)
- Classes
- Objects
- __init__()
- self
- Method Calls
- Refactoring Functions into a Class

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
- Main Menu
- Quiz Menu

Description:

A command-line flashcard application for learning German vocabulary.

The application is built using Object-Oriented Programming.
The GermanFlashcards class manages the vocabulary data,
file handling, vocabulary functions, and quiz system.

Vocabulary is stored in a dictionary and saved to a text file.
The data is automatically loaded when the program starts
and saved whenever vocabulary is added, updated, or removed.

The project was refactored from separate functions into
a GermanFlashcards class to better understand classes,
objects, self, method calls, and how a class can manage
related data and functionality.
"""


import random

class GermanFlashcards:
    def __init__(self):
        self.words = {}
        self.load_words()


    def load_words(self):
        try:
            file = open("vocabulary.txt", "r")
            for line in file:
                parts = line.strip().split(":")
                self.words[parts[0]] = parts[1]
            file.close()
        except:
            file = open("vocabulary.txt", "w")
            file.close()

    def save_words(self):
        file = open("vocabulary.txt", "w")
        for key, value in self.words.items():
            file.write(f"{key}:{value}\n")
        file.close()


    def header(self):
        print("==========================================")
        print("            GERMAN FLASHCARDS             ")
        print("==========================================")

    def show_menu(self):
        list_menu = ["Add Word", "Show Words", "Search Word",
                    "Update Word", "Remove Word", "Quiz", "Exit"]
        count = 1
        for menu in list_menu:
            print(f"{count}. {menu}")
            count += 1


    def check_dict_empty(self):
        return len(self.words) == 0
    

    def add_word(self):
        german_word = input("German: ")
        if german_word in self.words:
            print("This word already exists.")
            return
                
        english_word = input("English: ")
        self.words[german_word] = english_word
        print()
        print("Word added successfully.")
        self.save_words()

    def show_words(self):
        if self.check_dict_empty():
            print("No vocabulary yet.")
            return

        print("German Vocabulary")
        print()
        for key, value in self.words.items():
            print(f"{key} - {value}")

    def search_word(self):
        if self.check_dict_empty():
            print("No vocabulary yet.")
            return

        word_to_search = input("Search German word: ")
        if word_to_search in self.words:
            print(f"Meaning: {self.words[word_to_search]}")
        else:
            print("Word not found.")

    def update_word(self):
        if self.check_dict_empty():
            print("No vocabulary yet.")
            return

        word_to_update = input("German: ")
        if word_to_update not in self.words:
            print("This word does not exist.")
            return

        print(f"Current meaning: {self.words[word_to_update]}")
        print()
        self.words[word_to_update] = input("New English: ")
        print()
        print("Word updated successfully.")
        self.save_words()

    def remove_word(self):
        if self.check_dict_empty():
            print("No vocabulary yet.")
            return

        word_to_remove = input("German Word: ")
        if word_to_remove not in self.words:
            print("This word does not exist.")
            return

        self.words.pop(word_to_remove)
        print()
        print("Word removed successfully.")
        self.save_words()


    def quiz(self):
        if self.check_dict_empty():
            print("No vocabulary yet.")
            return

        while True:
            self.show_quiz_menu()
            print()
            choice = self.get_quiz_choice()
            print()

            if choice == 1:
                selected_words = self.prepare_question()
                score_count = self.DE_to_EN_questions(selected_words)
            elif choice == 2:
                selected_words = self.prepare_question()
                score_count = self.EN_to_DE_questions(selected_words)
            elif choice == 3:
                selected_words = self.prepare_question()
                score_count = self.mixed_questions(selected_words)
            elif choice == 4:
                return

            print(f"Your score is {score_count}/{len(selected_words)}.")
            print()

    def show_quiz_menu(self):
        print("======= QUIZ MENU =======")
        print()
        quiz_menu = ["German -> English", "English -> German", "Mixed", "Back"]
        count = 1
        for menu in quiz_menu:
            print(f"{count}. {menu}")
            count += 1

    def get_quiz_choice(self):
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

    def get_question_count(self):
        print(f"You have {len(self.words)} words.")
        print()
        while True:
            try:
                count_question = int(input("How many questions would you like?: "))
                if count_question < 1 or count_question > len(self.words):
                    print(f"You have only {len(self.words)} words. Please enter a number again.")
                    print()
                else:
                    return count_question
            except:
                print("Invalid input. Please enter a number.")
                continue

    def prepare_question(self):
        count_question = self.get_question_count()
        print()
        selected_words = self.random_words(count_question)
        return selected_words

    def random_words(self, count_question):
        words_list = list(self.words.items())
        selected_words = random.sample(words_list, count_question)
        return selected_words

    def DE_to_EN_questions(self, selected_words):
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

    def EN_to_DE_questions(self, selected_words):
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

    def mixed_questions(self, selected_words):
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

    def exit_text(self):
        print("Goodbye!")

flashcards = GermanFlashcards()
choice = 0

while choice != 7:
    flashcards.header()
    print()
    flashcards.show_menu()
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
        flashcards.add_word()
    elif choice == 2:
        flashcards.show_words()
    elif choice == 3:
        flashcards.search_word()
    elif choice == 4:
        flashcards.update_word()
    elif choice == 5:
        flashcards.remove_word()
    elif choice == 6:
        flashcards.quiz()
    elif choice == 7:
        flashcards.exit_text()
    print()