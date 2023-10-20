#!/usr/bin/python3

"""
Module that writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file, returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        char_written = file.write(text)
        return char_written
