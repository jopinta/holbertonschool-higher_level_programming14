#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """function should overwrite the content of the file"""

    with open("my_first_file.txt", 'w') as my_file:
        print(my_file.write("Holberton School is so cool!\n",))
