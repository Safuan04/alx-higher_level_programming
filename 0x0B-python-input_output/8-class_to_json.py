#!/usr/bin/python3
"""Defining a function called class_to_json"""


def class_to_json(obj):
    """This function returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object."""
    return vars(obj)
