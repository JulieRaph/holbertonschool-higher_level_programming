#!/usr/bin/python3
"""
This module to create a function that returns a list of lists
of integers representing the Pascal's triangle of n
"""


from math import factorial


def pascal_triangle(n):
    """
    Create a Pascal's triangle

    Args:
        n (int): always be an integer
        if n <= 0, return an empty list
    """
    n = 5

    if n <= 0:
        return []

    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i)//(factorial(j) * factorial(i-j)))

        print(row)
