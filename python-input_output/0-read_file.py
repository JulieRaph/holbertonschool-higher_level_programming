#!/usr/bin/python3
"""READ FILE"""


def read_file(filename=""):
    """Read a file text from my_file_o.txt"""
    with open("my_file_0.txt") as f:
        for line in f:
            print(line, end="")
