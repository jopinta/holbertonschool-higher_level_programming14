#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """function should overwrite the content of the file"""

    with open("filename", 'w', encoding="utf-8") as my_file:
        print(my_file.write(text))
