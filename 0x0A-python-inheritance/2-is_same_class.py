#!/usr/bin/python3

"""Defines a class function"""


def is_same_class(obj, a_class):
    """
    Initiate check to confirm if an object is an instance of a class

    Args:
        obj (any): Object to check
        a_class (type): Class to match the type of obj to check
    Returns:
        True - If obj is an instance of a_class
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
