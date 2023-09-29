#!/usr/bin/python3
"""Defining a function that finds the peak"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
