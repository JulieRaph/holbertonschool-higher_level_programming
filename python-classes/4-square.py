#!/usr/bin/python3
"""
This module to create a class square that defines a square by
the precedently tasks of the project
"""


class Square:
    """
    To define a square with private size

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    To define the area public of the square

    Return:
        The current square area
    """
    def area(self):
        return self.__size ** 2
