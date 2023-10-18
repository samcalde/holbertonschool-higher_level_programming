#!/usr/bin/python3

"""
Defines an BaseGeometry class
"""


class BaseGeometry:
    """
    Geometry class, with initial publice instance method
    """
    def area(self):
        """
        Raise exception of a method that's not implemented yet
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if (type(value) != int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
        return True
