#!/usr/bin/python3
""" appends a string at the end"""


def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open("file_append.txt", 'w') as my_file:
        my_file.write("Holberton School is so cool!/n")
