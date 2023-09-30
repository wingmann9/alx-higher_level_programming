#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Represents a Rectangle

    Attributes:
        number_of_instances (int): Number of Rectangle instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new instance of Rectangle

        Args:
            width(int): Width of the rectangle
            height(int): Height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Return printable representation of the Rectangle
        with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            if i < self.__height - 1:
                rectangle_str += "#" * self.__width + "\n"
            else:
                rectangle_str += "#" * self.__width
        return rectangle_str

    def __print__(self):
        """Return the str() for the Rectangle"""
        return __str__(self)

    def __repr__(self):
        """Return string representation of the Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a new for every instance deletion of Rectangle"""
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
