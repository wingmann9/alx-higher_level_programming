#!/usr/bin/python3
"""Defines a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle inherited from BaseGeometry"""

    def __init__(self, width, height):
        """
        Intialize a new Rectangle

        Args:
            width (int): Width of the new Rectangle.
            height (int): Height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
