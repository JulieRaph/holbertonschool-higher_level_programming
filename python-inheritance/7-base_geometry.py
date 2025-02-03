#!/usr/bin/python3
"""
This module contains a class BaseGeometry (based on 6-base_geometry.py)
and an integer_validator method
"""


class BaseGeometry:
    """
    A class BaseGeometry with an unimplemented area method
    and an integer_validator method
    """
    def area(self):
        """
        Raise:
            Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer

        Args:
            name (str): name of the parameter
            value (int): the parameter to validate

        Raise:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
