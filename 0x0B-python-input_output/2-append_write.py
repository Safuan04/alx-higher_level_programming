#!/usr/bin/python3
"""Define a function called append_write"""


def append_write(filename="", text=""):
    """this is a function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added"""

    with open(filename, 'a', encoding='utf-8') as a_file:

        file_append = a_file.write(text)

        return (file_append)
