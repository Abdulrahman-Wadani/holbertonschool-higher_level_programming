#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = matrix.copy()
    for i in range(0, len(matrix)):
        matrix[i] = list(map(lambda i: i * i, matrix[i]))
    return matrix
