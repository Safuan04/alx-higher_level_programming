#!/usr/bin/python3
"""Defining a function named is_kind_of_class"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
