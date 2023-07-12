#!/usr/bin/python3
"""module documentaion"""


class Student:
    """defines the class of a student"""
    def __init__(self, first_name, last_name, age):
        """initialize the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve instances"""
        return self.__dict__
