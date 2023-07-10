#!/usr/bin/python3
"""Defining a class named MyList"""


class MyList(list):
    """Subclass of list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
