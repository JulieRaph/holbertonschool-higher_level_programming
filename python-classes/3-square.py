#!/usr/bin/python3
"""
This module to create a class square that defines a square with size and area
"""


class Square:
    """
    Function to define a square with the size private

    Args:
        size = private instance attribute
        size = must be an integer
        size = must be bigger than 0

    Raise:
        TypeError = must be an integer
        ValueError = must be >= 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """
    To define the area public of the square

    Return:
        The current square area
    """
    def area(self):
        return self.__size ** 2
