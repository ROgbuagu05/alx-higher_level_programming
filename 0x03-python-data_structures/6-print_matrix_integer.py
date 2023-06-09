#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for row in matrix:
        for integer in row:
            print(str.format("{0}", integer), end=" ")
        print()
