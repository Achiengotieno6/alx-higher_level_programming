#!/usr/bin/python3
"""
creates object from JSON file
"""

import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”:"""
    with open(filename) as file:
        return json.load(file)
