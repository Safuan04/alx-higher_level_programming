#!/usr/bin/python3
"""This is a function that  reads a text file and prints it to stdout:"""


def read_file(filename=""):
"""This is a function that  reads a text file and prints it to stdout:"""

    with open(filename, encoding='utf-8') as a_file:

        file_read = a_file.read()

        print(file_read, end="")
