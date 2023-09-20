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

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = [[sum(a * b for a, b in zip(row, col))
                  for col in zip(*m_b)] for row in m_a]

    return new_matrix
