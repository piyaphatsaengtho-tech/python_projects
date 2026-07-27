"""
Project    : Germany Capitals Quiz
Author     : Pleng
Day        : Day 23
Language   : Python

Concepts:
- Functions
- Lists
- if / else
- while loop
- try / except
- Input Validation
- Membership operator (in)

Description:
A simple quiz game about the capitals of Germany.
Users answer three multiple-choice questions and receive
their final score at the end.
"""

## HEADER
def header():
    print("=============================================")
    print("          GERMANY CAPITALS QUIZ              ")
    print("=============================================")


## Q1
def question1():
    print("Was ist die Hauptstadt von Deutschland?")

def choice_question1():
    choices_Q1 = ["Berlin", "München", "Hamburg"]
    count = 1
    for choice in choices_Q1:
        print(count, choice)
        count += 1

def show_answer_Q1():
    while True:
        try:
            answer = int(input("Choose: "))
            if answer in [1, 2, 3]:
                return answer
            else:
                print("Invalid input.")
                print()
        except:
            print("Invalid input. Please enter a number of choice.")
            print()
            continue

def check_answer_Q1(answer_Q1):
    if answer_Q1 == 1:
        print("Correct!")
    else:
        print("Wrong!")
        print()
        print("The correct answer is:")
        print("Berlin")

def check_score_Q1(answer_Q1):
    if answer_Q1 == 1:
        return int(1)
    else:
        return int(0)


## Q2
def question2():
    print("Was ist die Hauptstadt von Hessen?")

def choice_question2():
    choices_Q1 = ["Frankfurt am Main", "Darmstadt", "Wiesbaden"]
    count = 1
    for choice in choices_Q1:
        print(count, choice)
        count += 1

def show_answer_Q2():
    while True:
        try:
            answer = int(input("Choose: "))
            if answer in [1, 2, 3]:
                return answer
            else:
                print("Invalid input.")
                print()
        except:
            print("Invalid input. Please enter a number of choice.")
            print()
            continue

def check_answer_Q2(answer_Q2):
    if answer_Q2 == 3:
        print("Correct!")
    else:
        print("Wrong!")
        print()
        print("The correct answer is:")
        print("Wiesbaden")

def check_score_Q2(answer_Q2):
    if answer_Q2 == 3:
        return int(1)
    else:
        return int(0)

## Q3
def question3():
    print("Was ist die Hauptstadt von Sachsen?")

def choice_question3():
    choices_Q1 = ["Leipzig", "Chemnitz", "Dresden"]
    count = 1
    for choice in choices_Q1:
        print(count, choice)
        count += 1

def show_answer_Q3():
    while True:
        try:
            answer = int(input("Choose: "))
            if answer in [1, 2, 3]:
                return answer
            else:
                print("Invalid input.")
                print()
        except:
            print("Invalid input. Please enter a number of choice.")
            print()
            continue

def check_answer_Q3(answer_Q3):
    if answer_Q3 == 3:
        print("Correct!")
    else:
        print("Wrong!")
        print()
        print("The correct answer is:")
        print("Dresden")

def check_score_Q3(answer_Q3):
    if answer_Q3 == 3:
        return int(1)
    else:
        return int(0)


## LINE
def line():
    print("-------------------------------------------------------------")


## End
def end_text():
    print("Quiz Finished!")


## CALCULATOR POINT
def show_all_point(score_Q1, score_Q2, score_Q3):
    score = score_Q1 + score_Q2 + score_Q3
    print("Your score: ", score, " / 3")


## RUN CODE
header()
print()

question1()
print()
choice_question1()
print()
answer_Q1 = show_answer_Q1()
print()
check_answer_Q1(answer_Q1)
print()

score_Q1 = check_score_Q1(answer_Q1)

line()
print()


question2()
print()
choice_question2()
print()
answer_Q2 = show_answer_Q2()
print()
check_answer_Q2(answer_Q2)
print()

score_Q2 = check_score_Q2(answer_Q2)

line()
print()

question3()
print()
choice_question3()
print()
answer_Q3 = show_answer_Q3()
print()
check_answer_Q3(answer_Q3)
print()

score_Q3 = check_score_Q3(answer_Q3)

line()
print()

end_text()
print()

show_all_point(score_Q1, score_Q2, score_Q3)