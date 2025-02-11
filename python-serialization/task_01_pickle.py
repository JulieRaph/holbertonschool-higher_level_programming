#!/usr/bin/python3
import pickle
"""
This module to serialize and deserialize custom
Python objects using the pickle module
"""


class CustomObject:
    """custom Python class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """To display that print out the object's attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is student: {}".format(self.is_student))

    def serialize(self, filename):
        """serialize a python dictionnary to JSON file"""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """deserialize the JSON file to recreate the Python dictionnary"""
        with open(filename, "rb")as file:
            loaded_object = pickle.load(file)
            return loaded_object
