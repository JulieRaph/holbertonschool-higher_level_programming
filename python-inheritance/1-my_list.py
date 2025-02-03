#!/usr/bin/python3
"""
This module to write a class MyList that inherits from list
"""


class MyList(list):
    def my_sum(self):
        if not all(isinstance(e, int) for e in self):
            raise TypeError("element must be an integer")
        return sum(i * e for i, e in enumerate(self))

    def print_sorted(self):
        if not all(isinstance(e, int) for e in self):
            raise TypeError("element must be an integer")
        print(sorted(self))
