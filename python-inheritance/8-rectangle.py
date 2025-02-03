#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py)
"""


class BaseGeometry:
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Print a class BaseGeometry with an integer_validator method and
    a private instance

    Args:
        width: a private instance positive int validated by integer_validator
        height: a private instance positive int validated by integer_validator
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
