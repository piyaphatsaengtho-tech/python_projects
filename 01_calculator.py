# ====================================================
# Project : Calculator
# Day : 7
# Author : Pleng
# Language: Python
# Description: A simple calculator that performs
# addition, subtraction, multiplication and divition
# using functions and if-elif-else statements.
# =====================================================

print("====== Calculator =====")
print()

a = int(input("Number 1: "))
b = int(input("Number 2: "))

print()

print("Choose")
print("1. +")
print("2. -")
print("3. ×")
print("4. ÷")
print()

choose = int(input("Your choice: "))

def add(a,b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  if b == 0:
    return "Cannot divide by zero."
  return a / b

answer = None

if choose == 1:
  answer = add(a, b)
elif choose == 2:
  answer = subtract(a, b)
elif choose == 3:
  answer = multiply(a, b)
elif choose == 4:
  answer = divide(a, b)
else:
  print("Invalid choice")

if answer is not None:
  print("The answer is ", answer)
