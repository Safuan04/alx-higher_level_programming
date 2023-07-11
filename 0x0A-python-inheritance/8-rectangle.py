#!/usr/bin/python3
"""Define a class named Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Define a class named Rectangle"""


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""
    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", self.__width)
        self.__height = height
        self.integer_validator("height", self.__height)
