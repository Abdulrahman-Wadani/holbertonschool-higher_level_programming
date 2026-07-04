#!/usr/bin/python3
"""
This module defines the Student class.
"""


def pascal_triangle(n):
    """ Function that returns a list of lists of integers"""
    tri = [[1]]
    for i in range(1, n):
        prev = tri[i - 1]
        newl = [1]
        for j in range(len(prev) - 1):
            newl.append(prev[j] + prev[j + 1])
        newl.append(1)
        tri.append(newl)
    return tri if n > 0 else []
