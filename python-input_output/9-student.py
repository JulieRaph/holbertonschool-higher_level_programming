#!/usr/bin/python3
"""
This module to write a class Student that defines a student
by public instance attribute
"""


class Student:
    """Define Class Student"""

    def __init__(self, first_name, last_name, age):
        """
        Define public instance attribute

        Args:
            first_name (str): public attribute
            last_name (str): public attribute
            age (int): public attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance"""
        return self.__dict__
