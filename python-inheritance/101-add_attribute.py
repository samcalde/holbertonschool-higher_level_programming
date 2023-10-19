#!/usr/bin/python3

"""
Define a function that adds a new attribute to an object
"""


def add_attribute(obj, att_name, att_value):
    """
    Adds an attribute to an object after checking if it's possible
    """
    if (hasattr(obj, '__slots__') and att_name not in obj.__slots__):
        raise TypeError("can't add new attribute")
    elif (issubclass(obj.__class__, (str, int, float, tuple, bool, frozenset))):
        setattr(obj, att_name, att_value)
    else:
        raise TypeError("can't add new attribute")
