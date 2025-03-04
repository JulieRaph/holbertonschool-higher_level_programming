#!/usr/bin/python3
"""
This module to write a class Student that defines a student by:
(based on 9-student.py) with filter
"""


class Student:
    """Define class Student"""

    def __init__(self, first_name, last_name, age):
        """
        Define public instance attribute

        Args:
            first_name (str): public attribute first name student
            last_name (str): public attribute last name student
            age (int): public attribute age student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Args:
            attrs: is a list of strings, only attribute names
            contained in the list must be retrieved

        Return:
            dict: A dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__.copy()
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict
