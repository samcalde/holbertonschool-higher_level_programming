#!/usr/bin/python3

"""
Defines a class called rectangle
"""


class Rectangle:
    """
    Class called rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Returns height of rectangle
        """
        return self.__height

    @property
    def width(self):
        """
        Returns width of rectangle
        """
        return self.__width

    @height.setter
    def height(self, value):
        """
        Height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        Width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value
