#!/usr/bin/python3
"""
Module to create a class rectangle that define a rectangle by 6-rectangle.py
"""


class Rectangle:
    """
    Function to create a rectangle with character # and new
    instance eval

    Property:
        width: private attribute instance
        height: private attribute instance

    Raise:
        TypeError: width and height must be an integer
        ValueError: width and height mus be >= 0

    Public classe method:
       number_of_instances = initialized to 0
       print_symbol = initialized to #

    Public instance:
        area and perimeter of the rectangle to return

    Return:
        Rectangle printed with the character # and eval

    Methods:
        str, repr, del
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = self.print_symbol

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rectangle = ""
            for i in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    rectangle += "\n"
            return rectangle

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
