#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b

    Float args are typecasted into int before addition is performed

    Raises:
        TypeError: if either a or b is a non-integer or non-float
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
