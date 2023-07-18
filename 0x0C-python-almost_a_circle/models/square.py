#!/usr/bin/python3
"""Importing the rectangle class"""

from models.rectangle import Rectangle


"""Define a class named square"""


class Square(Rectangle):
    """This is a class named Square that inherit from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """this is getter"""

        return self.__size

    @size.setter
    def size(self, value):
        """this is a setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """This is amethod that return the string repre of a rectangle"""

        return ("[Square] ({}) {}/{} - {}". format(self.id,
                self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """this is a method that that assigns attributes"""

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        if args is not None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """this is a method that
        returns the dictionary representation of a Square"""

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
