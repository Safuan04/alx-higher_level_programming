#!/usr/bin/python3
"""Defining a function named is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """checks  if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class"""

    if issubclass(type(obj), a_class):
        return True
    else:
        return False
