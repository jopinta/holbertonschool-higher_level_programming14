#!/usr/bin/python3
"""Public instance method"""


class BaseGeometry:
    """need to comment"""

    def area(self):
        """to calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """we aware of validation"""
        if (type(value) != int)
        raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
