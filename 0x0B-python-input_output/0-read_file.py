#!/usr/bin/python3
"""
Reads a text file
"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print('{}'.format(line), end='')
