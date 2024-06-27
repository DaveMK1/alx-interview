#!/usr/bin/python3
"""
A module for working with Pascal's triangle
"""


def pascal_triangle(n):
    """Creates a list of lists of integers representing
    the Pascal's triangle of a given integer
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            triangle.append(level)
    return triangle
