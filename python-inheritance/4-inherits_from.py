#!/usr/bin/python3

"""
Checks if the object is a subclass
"""


def inherits_from(obj, a_class):
    """
    Function that does what is specified above
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
