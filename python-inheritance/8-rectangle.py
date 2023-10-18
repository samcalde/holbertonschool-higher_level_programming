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
