#!/usr/bin/python3
"""module documentation"""


def class_to_json(obj):
    """
    a function that returns the dictionary description
    for JSON serialization of an object:
    """
    return obj.__dict__
