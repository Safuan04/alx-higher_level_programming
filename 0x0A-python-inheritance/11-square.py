#!/usr/bin/python3
"""import a class named Rectangle to inherit from it"""


Rectangle = __import__('9-rectangle').Rectangle


"""Define a class named Square that inherits from Rectangle"""


class Square(Rectangle):
    """Instantiation with size"""

    def __init__(self, size):
        self.__size = size

        self.integer_validator("size", size)

        super().__init__(size, size)

    def __str__(self):
        """the square description"""

        return ("[Square] {}/{}".format(self.__size, self.__size))
