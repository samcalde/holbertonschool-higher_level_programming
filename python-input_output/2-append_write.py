#!/usr/bin/python3

"""
Module that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    Appends text at the end of a file, returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file:
        char_added = file.write(text)
        return char_added
