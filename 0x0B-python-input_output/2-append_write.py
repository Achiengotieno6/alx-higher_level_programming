#!/usr/bin/python3
"""
Append string
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, 'a') as file:
        return file.write(text)
