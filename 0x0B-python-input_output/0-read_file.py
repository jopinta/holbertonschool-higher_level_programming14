#!/usr/bin/python3
""" that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """ use the with statement"""

    with open(filename, mode='r', encoding='utf-8') as my_file:
        print(my_file.read(), end="")
