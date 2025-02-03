#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py)
(task based on 8-rectangle.py)
"""


class BaseGeometry:
    """
    Implemantation 7-base_geometry.py function
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Print a rectangle with an area of the rectangle

    Args:
        width: private positive integers validated by integer_validator
        height: private positive integers validated by integer_validator

    Return:
        area of the rectangle
        __str__ function to divide width and height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
