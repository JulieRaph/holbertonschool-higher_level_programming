#!/usr/bin/python3
"""
This module to load, add, save
"""


import json
import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""
Function to write a script that adds all arguments to a 
Python list, and then save them to a file
"""

if __name__ == "__main__":
    filename = "add_item.json"

    my_list = []

    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)
    save_to_json_file(my_list, filename)
