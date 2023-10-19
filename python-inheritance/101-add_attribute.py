#!/usr/bin/python3

"""
Define a function that adds a new attribute to an object
"""


def add_attribute(obj, att_name, att_value):
    """
    Adds an attribute to an object after checking if it's possible
    """
    if isinstance(obj, (str, int, float, tuple, bool, frozenset)):
        raise TypeError("can't add new attribute")
    setattr(obj, att_name, att_value)
