#!/usr/bin/python3
"""
    To define a function that prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first name> <last name>"

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raise:
        TypeError: if first_name and last_name are not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
