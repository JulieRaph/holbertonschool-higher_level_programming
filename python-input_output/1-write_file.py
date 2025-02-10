#!/usr/bin/python3
"""
This module to Write to a file
"""


def write_file(filename="", text=""):
    """
    write a string to a text file and returns the nber of char written

    Args:
        filename (str): The name of the file
        text (str): The string to write to the file

    Return:
        The numbers of the characters
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
