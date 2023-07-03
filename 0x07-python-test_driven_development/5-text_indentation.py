#!/usr/bin/python3
def text_indentation(text):
    """ prints a text with 2 new lines after: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    checker = 0

    while checker < len(text) and text[checker] == " ":
        checker += 1

    while checker < len(text):
        print(text[checker], end="")
        if text[checker] in ["\n", ".", "?", ":"]:
            if text[checker] in [".", "?", ":"]:
                print("\n")
            checker += 1
            while checker < len(text) and text[checker] == " ":
                checker += 1
            continue
        checker += 1
