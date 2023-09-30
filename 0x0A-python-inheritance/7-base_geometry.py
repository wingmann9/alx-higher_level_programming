#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Reprsent a geometry"""

    def area(self):
        """Function not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a function parameter as an integer

        Args:
            name (str): Name of the parameter
            value (int): Parameter to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
