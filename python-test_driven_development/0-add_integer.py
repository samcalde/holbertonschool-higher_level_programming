#!/usr/bin/python3

"""
Function that adds 2 ints
"""


def add_integer(a, b=98):
    """
    Adds int a with int b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if not (type(a) == int):
        raise TypeError("a must be an integer")
    if not (type(b) == int):
        raise TypeError("b must be an integer")
    return a + b
