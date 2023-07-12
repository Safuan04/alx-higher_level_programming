#!/usr/bin/python3
"""Define a function called write_file"""


def write_file(filename="", text=""):
    """This is a function that writes a string to a text file (UTF8)
       and returns the number of characters written"""

    with open(filename, 'w', encoding='utf-8') as a_file:

        file_write = a_file.write(text)

        return (file_write)
