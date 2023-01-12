#!/usr/bin/python3

# Function computes square of integers of a matrix using map()
def square_matrix_map(matrix=[]):

    # Using list(), map() & lambda() to return square of matrix
    return (list(map(lambda i: list(map(lambda x: x**2, i[:])), matrix)))
