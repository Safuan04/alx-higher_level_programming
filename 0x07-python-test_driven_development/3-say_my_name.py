#!/usr/bin/python3
""" Defining a function called say_my_name """


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("Last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
