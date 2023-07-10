#!/usr/bin/python3
"""Defining a function named is_same_class"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    else:
        return False
