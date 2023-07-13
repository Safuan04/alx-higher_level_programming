#!/usr/bin/python3
"""Defining a class called Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This function retrieves a
        dictionary representation of a Student instance"""

        return vars(self)
