#!/usr/bin/python3
"""square stuff"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square restro"""
    def __init__(self, size):

        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)


    def __str__(self):
        """str str"""
return "[square] {}/{}".format(self.__size, self.__size)
