#!/usr/bin/python3
"""Define a class"""


class Square:
    """Initializes the size with 2 conditiions,
        one for the sizes type and the other for the sizes value"""
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """Calculate the area of the sqaure"""
    def area(self):
        return self.__size * self.__size
