#!/usr/bin/python3
"""inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file
    after each line containing a specific string
    """
    with open(filename, 'r') as f:
        for line in f:
            text = text + line
            if search_string in line:
                text = text + new_string

    with open(filename, 'w') as k:
        k.write(text)
