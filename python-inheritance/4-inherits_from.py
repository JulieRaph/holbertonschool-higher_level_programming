#!/usr/bin/python3
"""This module to write a function that True if the object is an instance"""


def inherits_from(obj, a_class):
    """
    Print if the object is an instance of a class that
    inherited from (directly or indirectly)

    Args:
        obj: The object to check
        a_class: The class to compare against

    Return:
        True if obj is an instance of a class that inherited from a_class;
        otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
