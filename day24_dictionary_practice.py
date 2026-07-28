"""
Practice   : Dictionary Practice
Author     : Pleng
Day        : Day 24
Language   : Python

Concepts:
- Dictionary
- Keys & Values
- .get()
- .items()
- for loop

Description:
Practice creating, updating, accessing, and displaying data
using Python dictionaries.
"""


profile = {
    "name": "Pleng",
    "age": 23,
    "country": "Thailand"
}

profile["language"] = "German"
profile["job"] = "Student"
profile["age"] = 24


def show_profile(profile):
    for key, value in profile.items():
        print(f"{key}: {value}")


show_profile(profile)