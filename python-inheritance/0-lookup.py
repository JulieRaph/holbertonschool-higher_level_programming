#!/usr/bin/python3
"""
This module to print the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Print the list of available attributes
    and methods of an object
    """
    return dir(obj)
