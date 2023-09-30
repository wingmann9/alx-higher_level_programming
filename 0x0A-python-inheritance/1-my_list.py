#!/usr/bin/python3
"""Prints a list in ascending order"""


class MyList(list):
    """
    A class to modify the list class
    """

    def print_sorted(self):
        """
        Sorts and prints a list in ascending order
        """
        if issubclass(MyList, list):
            print(sorted(self))
