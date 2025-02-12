#!/usr/bin/python3
"""
This module to create a function that returns a list of lists
of integers representing the Pascal's triangle of n
"""


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

    pascal_triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(pascal_triangle[i - 1][j - 1]+pascal_triangle[i - 1][j])
        row.append(1)
        pascal_triangle.append(row)

    return pascal_triangle
