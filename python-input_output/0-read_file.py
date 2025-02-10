#!/usr/bin/python3
"""READ FILE"""


def read_file(filename=""):
    """
    Read a file text from my_file_o.txt

    Args:
        filename (str): text to read
    """
    with open(filename, encoding="utf-8") as f:

        print(f.read(), end="")
