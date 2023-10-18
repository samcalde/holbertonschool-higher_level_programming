#!/usr/bin/python3

"""
Defines class Rectangle that inherits from BaseGeometry
"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def area(self):
        """
        Implementation of area
        """
        return (self.__width * self.__height)
    
    def __str__(self):
        """
        Returns rectangle description
        """
        return (f"[{__class__.__name__}] {self.__width}/{self.__height}")
