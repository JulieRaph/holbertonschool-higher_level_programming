#!/usr/bin/python3
"""
This module to write a class BaseGeometry (based on 5-base_geometry.py)
"""


class BaseGeometry:
    """
    Print a class BaseGeometry with an unimplemented area method

    Raise:
        Exception: area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
