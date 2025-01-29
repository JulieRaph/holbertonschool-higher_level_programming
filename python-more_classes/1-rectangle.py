#!/usr/bin/python3
"""
Module to write a class rectangle that define a rectangle by 0-rectangle.py
"""


class Rectangle:
    """
    Function to define a rectangle with widht and height

    Property:
        width: private attribute instance
        height: private attribute instance

    Raise:
        TypeError: width and height must be an integer
        ValueError: width and height must be >= 0
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
