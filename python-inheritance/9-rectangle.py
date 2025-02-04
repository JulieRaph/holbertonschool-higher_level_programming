#!/usr/bin/python3
"""This module contains a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Print a rectangle with an area of the rectangle"""

    def __init__(self, width, height):
        """
        Args:
            width: private positive integers validated by integer_validator
            height: private positive integers validated by integer_validator

        Return:
            area of the rectangle
            __str__ function to divide width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
