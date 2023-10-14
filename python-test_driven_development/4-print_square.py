#!/usr/bin/python3

"""
Function that prints a square with the character #
"""


def print_square(size):
    """
    Function that prints the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for columns in range(0, size):
        for rows in range(0, size):
            print("#", end="")
        print("")
