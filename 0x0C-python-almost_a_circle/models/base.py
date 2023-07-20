#!/usr/bin/python3
"""module documentation of class Base"""


class Base:
    """defines a super class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
