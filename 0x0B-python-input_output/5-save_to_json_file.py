#!/usr/bin/python3
"""Defining a function called save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """this is a function that writes an Object to a text file,
    using a JSON representation."""

    with open(filename, "w", encoding="utf-8") as File:

        File.write(json.dumps(my_obj))
