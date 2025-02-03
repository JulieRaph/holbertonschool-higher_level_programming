#!/usr/bin/python3
"""
This module to write a function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Print if the object is an instance of a class that
    inherited from (directly or indirectly)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
