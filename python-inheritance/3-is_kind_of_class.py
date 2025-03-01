#!/usr/bin/python3
"""
This module to write a function that returns True if the object is an instance
of, or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Print if the object is an instance of a class that
    inherited from
    """
    if type(obj) is a_class:
        return True
    elif isinstance(obj, a_class):
        return True
    else:
        return False
