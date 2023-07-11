#!/usr/bin/python3
"""A class MyInt that inherits from int"""


class MyInt(int):
    """A subclass of class int"""
    def __eq__(self, other):
        """sets the equality (==) comparison"""
        return int(self) != other

    def __ne__(self, other):
        """sets the inequality (!=) behavior"""
        return int(self) == other
