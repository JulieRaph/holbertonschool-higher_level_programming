#!/usr/bin/python3
"""Shapes, Interfaces, and Duck Typing"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape"""
    @abstractmethod
    def area(self):
        """Abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method perimeter"""
        pass


class Circle(Shape):
    """Subclass circle from Shape"""
    def __init__(self, radius):
        """initialize the circle object with a given radius"""
        self.radius = radius

    def area(self):
        """calculate circle area"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """calculate circle perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Subclass rectangle from Shape"""
    def __init__(self, width, height):
        """initialize the Rectangle object with given height and width"""
        self.width = width
        self.height = height

    def area(self):
        """calculate the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """calculate the rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """print area and perimeter"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
