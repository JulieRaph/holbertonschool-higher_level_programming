#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


class BaseGeometry:
    """A class BaseGeometry"""

    def area(self):
        """Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer

        Args:
            name (str): name of the parameter
            value (int): the parameter to validate

        Raise:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
