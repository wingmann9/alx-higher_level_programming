#!/usr/bin/python3
# 100-matrix_mul.py
"""Defines a matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices

    Args:
        m_a (list of lists of int/float): First matrix
        m_b (list of lists of int/float): Second matrix

    Raises:
        TypeError: If either m_a or m_b is not a list
        TypeError: If either m_a or m_b is not a matrix
        TypeError: If either m_a or m_b is not list of lists of int/float
        ValueError: If either m_a or m_b is empty
        TypeError: If either m_a or m_b has different-sized rows
        ValueError: If m_a and m_b cannot be multiplied

    Returns:
        A new matrix of m_a * m_b
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    else:
        if not all(isinstance(row, list) for row in m_a):
            raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    else:
        if not all(isinstance(row, list) for row in m_b):
            raise TypeError("m_b must be a list of lists")

    if not all(isinstance(e, (int, float)) for row in m_a for e in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(e, (int, float)) for row in m_b for e in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for row in range(len(m_b[0])):
        new_row = []
        for col in range(len(m_b)):
            new_row.append(m_b[col][row])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
