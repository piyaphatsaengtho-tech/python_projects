"""
Practice   : Object-Oriented Programming (OOP)
Author     : Pleng
Day        : Day 36
Language   : Python

Concepts:

- Class
- Object
- Attributes
- Methods
- __init__()
- self
- return
- Encapsulation
- Inheritance
- super()

Description:
Practice the basic concepts of Object-Oriented Programming
by creating classes, objects, attributes, and methods.
Also practice encapsulation, inheritance, and using super()
to initialize attributes from a parent class.
"""

# 1. Class, Object, Attributes and Methods
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

    def change_author(self, new_author):
        self.author = new_author

    def get_info(self):
        return f"{self.title} by {self.author}"


book1 = Book("Harry Potter", "J.K.")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("1984", "George Orwell")

book1.change_author("J.K. Rowling")

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())


# 2. Encapsulation
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

account1 = BankAccount(1000)
account1.deposit(500)

print(account1._balance)


# 3. Inheritance
class Animal:
    def eat(self):
        print("I can eat")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog1 = Dog()
dog1.eat()
dog1.bark()


# 4. Inheritance with super()
class AnimalWithName:
    def __init__(self, name):
        self.name = name

class DogWithBreed(AnimalWithName):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog2 = DogWithBreed("Buddy", "Golden Retriever")

print(dog2.name)
print(dog2.breed)