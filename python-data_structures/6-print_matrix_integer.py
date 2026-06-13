#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(i) == 0:
            print()
        for j in range(0, len(i)):
            print("{:d}".format(i[j]), end=" " if j != i[len(i) - 1] else "\n")
