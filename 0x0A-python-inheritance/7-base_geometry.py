#!/usr/bin/python3
"""creates an empty class"""


class BaseGeometry:
    """defines the class BaseGeometry"""

def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """validates the value"""
    if (not type(value) is int):
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must b greater than 0".format(name))
