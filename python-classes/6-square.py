#!/usr/bin/python3
"""
This module to create a class square that defines a square
by the task  (5-square.py)
"""


class Square:
    """
    Function to define a square with private size and private position

    Raise:
        TypeError = size must be an integer
        ValueError = size must be >= 0
        TypeError = position must be a tuple of 2 positive integers

    Property:
        to retrieve it = def size(self) and def position(self)
        to set it = def size(self, value) and def position(self, value)
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

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
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
