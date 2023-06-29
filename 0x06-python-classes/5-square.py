#!/usr/bin/python3
"""Define a class"""


class Square:
    """Initializes the size with 2 conditiions,
        one for the sizes type and the other for the sizes value"""
    def __init__(self, size=0):
        self.__size = size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    """Calculate the area of the sqaure"""
    def area(self):
        return self.__size * self.__size

    """ prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
