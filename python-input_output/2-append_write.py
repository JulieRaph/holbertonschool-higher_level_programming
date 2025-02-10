#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """append a string at the end of a text file
        and return the nber of char added
        """
    with open("file_append.txt", mode="a", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
