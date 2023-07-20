#!/usr/bin/python3
"""module documentaion"""


class Student:
    """defines the class of a student"""
    def __init__(self, first_name, last_name, age):
        """initialize the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve instance Student"""
        if attrs is None:
            return self.__dict__

        else:
            d = {}
            for attr in attrs:
                if hasattr(self, attr):
                    d[attr] = getattr(self, attr)
            return d
