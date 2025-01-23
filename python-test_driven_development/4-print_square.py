#!/usr/bin/python3
"""
    This module define a function that print a square with the character #
"""


def print_square(size):
    """
    Print a square with the character #

    Args:
        size (int): The size lenght of the square.

    Raise:
        TypeError: if the size is not an integer
        ValueError: if the size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
