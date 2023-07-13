#!/usr/bin/python3
"""Defining a function called from_json_string"""


import json


def from_json_string(my_str):
    """this is a function that returns an object (Python data structure)"""

    return json.loads(my_str)
