#!/usr/bin/python3
"""
This module to Class to JSON
"""


import json


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple
    data structure for JSON serialization of an object

    Args:
        obj: is an instance of a Class

    Return:
        Dictionnary simple data structure (int, str, bool...)
    """
    return obj.__dict__
