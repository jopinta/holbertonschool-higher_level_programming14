#!/usr/bin/python3


class Rectangle:

    def __init__(self, width=0, height=0):
        """ function to define a rectangle"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ kkksdknfks"""
        return self.__height

    @height.setter
    def height(self, value):
        """ escribir algo"""
        if type(value) =! int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """puede ser"""
        return self.__width

    @width.setter
    def width(self, value):
        """property to set with"""
        if type(value) != int:
            raise TypeError("must be an integer")

        elif value < 0:
            raise ValueError("must be >= 0")
        self.__width = value
