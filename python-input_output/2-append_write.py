#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """
    append a string at the end of a text file
    and return the nber of char added

    Args:
        filename (str): Text file
        text (str) : text to append at the end of the file

    Return:
        number of the characters
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
