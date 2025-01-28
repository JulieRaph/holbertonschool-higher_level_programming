#!/usr/bin/python3
"""
This module to create a class square that defines a square
by the task 4 (4-square.py) and print the square
"""


class Square:
    """
    Function to defines a square with private size

    Raise:
        TypeError = size must be an integer
        ValueError = size must be >= 0

    Property:
        to retrieve it = def size(self)
        to set it = def size(self, value)
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    To define a public area of the square

    Return:
        The current of the square
    """
    def area(self):
        return self.__size ** 2

    """
    To print in stdout the square with the character '#'

    Args:
        size = if size is equal to 0, print an empty line
    """
    def my_print(self):
        if self.__size == 0:
            print(" ")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
