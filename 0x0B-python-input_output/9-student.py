#!/usr/bin/python3
""" instance of an object"""


class Student:
    """new class"""

    def __init__(self, first_name, last_name, age):
        """constructor fun"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary description"""
        return (self.__dict__)
