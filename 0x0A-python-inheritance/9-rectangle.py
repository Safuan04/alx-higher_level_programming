#!/usr/bin/python3
"""Define a class named Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Define a class named Rectangle"""


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""
    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)

        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """calculate the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
