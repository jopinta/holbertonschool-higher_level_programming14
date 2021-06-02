#!/usr/bin/python3
""" that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """ use the with statement"""

    with open("my_file_0.txt", 'r', encoding="utf-8") as my_file:
        print(my_file.read())
