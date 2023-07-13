#!/usr/bin/python3
"""Defining a function called to_json_string"""


import json


def to_json_string(my_obj):
    """this is function that returns the JSON representation of"""

    return json.dumps(my_obj)
