# ==================================================================================
# Project : Guess the Number
# Day : 8
# Author : Pleng
# Language : Python
#
# Description: A simpl guessing game using while loops and if-elif-else statements.
# ==================================================================================

print("===== GUESS THE NUMBER! =====")

secret_number = 7
guess = 0

while guess != secret_number:
  print()
  guess = int(input("Guess the number: "))
  if guess == secret_number:
    print("Correct!")
    print("You win!")
  else:
    print("Wrong!")
    if guess < secret_number:
      print("Too low!")
    else:
      print("Too high!")
