#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle
"""Defines a Rectangle subclass Square"""


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """
        Initialize a new square.

        Args:
            size (int): Size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
