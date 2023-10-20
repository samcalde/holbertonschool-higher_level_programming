#!/usr/bin/python3

"""
Creates dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    """
    return (vars(obj))
