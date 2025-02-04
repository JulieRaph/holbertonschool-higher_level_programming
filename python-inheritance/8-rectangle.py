#!/usr/bin/python3
"""This module contains a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
