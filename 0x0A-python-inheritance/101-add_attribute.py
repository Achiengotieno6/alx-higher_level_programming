#!/usr/bin/python3
"""module documentation"""


def add_attribute(obj, name, value):
    """This methond adds an attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
