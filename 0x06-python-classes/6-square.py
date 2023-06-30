#!/usr/bin/python3
"""Define a class"""


class Square:
    """Initializes the size with 2 conditiions,
        one for the sizes type and the other for the sizes value"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, int) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                f value[0] > 0 and value[1] > 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """Calculate the area of the sqaure"""
    def area(self):
        return self.__size * self.__size

    """ prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            i, j = self.__position
        for _ in range(j):
            print()
        for _ in range(self.__size):
            print(" " * i + self.__size * "#")
