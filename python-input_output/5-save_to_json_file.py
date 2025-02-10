#!/usr/bin/python3
"""Save Object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """
    function to write an Obj to a text file, using a JSON representation

    Args:
        my_obj: The object to be serialized and written to the file
        filename (str): The name of the file to write to
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
