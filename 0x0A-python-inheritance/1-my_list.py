#!/usr/bin/python3

"""The module inherits from list"""


class MyList(list):
    """Defines a subclass of list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
