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
        for key in self.__dict__:
            print("{} : {}".format(key.capitalize(), self.__dict__[key]))

    def serialize(self, filename):
        """serialize a python dictionnary to JSON file"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PickleError) as e:
            print("Serialization error: {}".format(e))
            return None

    @classmethod
    def deserialize(cls, filename):
        """deserialize the JSON file to recreate the Python dictionnary"""
        try:
            with open(filename, "rb")as file:
                loaded_object = pickle.load(file)
                return loaded_object
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print("Deserialization error: {}".format(e))
            return None
