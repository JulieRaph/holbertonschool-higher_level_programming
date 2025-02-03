#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle
(9-rectangle.py)
"""


class BaseGeometry:
    """
    Implementation integer_validator and area method
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Square(BaseGeometry):
    """
    Class representing a square, inheriting from BaseGeometry
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size
