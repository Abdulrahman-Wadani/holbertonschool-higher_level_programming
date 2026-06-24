#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains one function `matrix_divided(matrix, div)` that divides all
elements of a matrix by a given number and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The matrix containing ints or floats.
        div (int/float): The number to divide the matrix by.

    Returns:
        list of lists: A new matrix with the divided elements rounded to
        2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of ints/floats.
        TypeError: If the rows of the matrix are not the same size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix is a list and not empty
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(error_msg)

    for row in matrix:
        # Check if each row is a list
        if type(row) is not list or len(row) == 0:
            raise TypeError(error_msg)
        # Check if elements are ints or floats
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(error_msg)

    # Check if all rows are the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix with values divided and rounded to 2 decimal places
    return [[round(item / div, 2) for item in row] for row in matrix]
