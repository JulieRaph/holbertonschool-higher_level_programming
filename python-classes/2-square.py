#!/usr/bin/python3
"""
This module to write a class square that defines a square by task 1
"""


class Square:
    """
    Function to define a square with the size of the square

    Args:
        size = private instance attribute
        size = must be an integer
        size = must be bigger than 0

    Raise:
        TypeError = size must be an integer
        ValueError = size must be >= 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
