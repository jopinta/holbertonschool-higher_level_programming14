#!/usr/bin/python3
"""class Node that defines a node of a sll"""


class Node:
    """class node that defines a node of a sll"""

    def __init__(self, data, next_node=None):
        """Instantiation with data and nex_node"""
        self.__data = data

    @property
    def next_node(self):
        """property to retrieve it"""
        return self.__next_node

    @size.setter
    def next_node(self, value):
        """property setter to set it"""
        if type(value) is node || None:
            if value >= 0:
                self.__next_node = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("next_node must be a Node object")

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
