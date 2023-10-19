#!/usr/bin/python3

def add_attribute(obj, att_name, att_value):
    if isinstance(obj, (str, int, float, tuple, bool, frozenset)):
        raise TypeError("can't add new attribute")
    setattr(obj, att_name, att_value)
