#!/usr/bin/python3
"""This module contains a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square, inheriting from BaseGeometry"""

    def __init__(self, size):
        """
        Initialize a square instance

        Args:
            size (int): The size of the square's size

        Raise:
            Exception
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area"""
        return (self.__size * self.__size)

    def __str__(self):
        """Return a string representation of the square"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
