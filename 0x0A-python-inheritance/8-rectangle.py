#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Define a class Rectangle with BaseGeometry inheritance"""


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """
        Intialize a new Rectangle

        Args:
            width (int): Width of the new Rectangle
            height (int): Height of the new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
