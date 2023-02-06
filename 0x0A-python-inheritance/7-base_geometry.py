#!/usr/bin/python3

"""Define class BaseGeometry"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """Define area() and raise Exception to not implement"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a parameter as an integer

        Args:
            name (str): Name of the parameter
            value (int): Parameter to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
