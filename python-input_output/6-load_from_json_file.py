#!/usr/bin/python3
"""Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file

    Args:
        filename (str): JSON file name

    Return:
        object created from JSON
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
