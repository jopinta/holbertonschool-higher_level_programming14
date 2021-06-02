#!/usr/bin/python3
""" appends a string at the end"""


def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as my_file:
        return my_file.write(text)
