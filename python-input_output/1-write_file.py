#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """ write a string to a text file and returns the nber of char written"""
    with open("my_first_file.txt", mode="w", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
