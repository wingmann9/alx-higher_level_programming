#!/usr/bin/python3

# Function compute the square value of all integers in a matrix
def square_matrix_simple(matrix=[]):

    # iterate the square of each element using map() and lambda()
    return (list(map(lambda i: list(map(lambda x: (x**2), i)), matrix)))
