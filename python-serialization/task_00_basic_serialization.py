#!/usr/bin/python3
"""
This module to create a basic serialization that adds the functionality to
serialize a Python dictionnary to a JSON file and deserialize the JSON
"""


import pickle


def serialize_and_save_to_file(data, filename):
    """serialize a Python dictionnary to a JSON file"""
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """deserialize the JSON file to recreate the Python dictionnary"""
    with open(filename, "rb") as file:
        loaded_data = pickle.load(file)
    return loaded_data
