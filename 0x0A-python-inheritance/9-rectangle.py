#!/usr/bin/python3
"""rectangulo"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is a rectangle"""


def __init__(self, width, height):
        """instantation of"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


def area(self):
    """area """
    return (self.__width * self.__height)


def __str__(self):
    """this is the rectan"""
    return "[rectangle] {}/{}".format(self.__width, self.__height)
