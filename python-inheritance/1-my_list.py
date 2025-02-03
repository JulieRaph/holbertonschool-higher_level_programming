#!/usr/bin/python3
"""
This module to write a class MyList that inherits from list
"""


class MyList(list):
    def my_sum(self):
        return sum(i * e for i, e in enumerate(self))

    def print_sorted(self):
        print(sorted(self))
