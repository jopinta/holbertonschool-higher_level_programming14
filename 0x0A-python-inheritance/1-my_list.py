#!/usr/bin/python3
"""Public instance method: def print_sorted(self)"""


class Mylist(list):

    """MyList that inherits from list"""

    def print_sorted(self):
        """prints the list but sorted """
        print(sorted(self))
