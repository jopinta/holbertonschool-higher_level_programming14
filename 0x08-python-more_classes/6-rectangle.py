#!/usr/bin/python3
"""
Module for task 6
"""


class Rectangle:
    """Defines a Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiation attributes"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
