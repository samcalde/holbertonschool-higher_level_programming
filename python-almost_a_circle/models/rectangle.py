#!/usr/bin/python3

"""
Module defines the Rectangle class, which inherits from Base in base.py
"""


from models.base import Base
class Rectangle(Base):
    """
    Definition of the Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Returns width of the Rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Returns height of the Rectangle
        """
        return self.__height

    @property
    def x(self):
        """
        Returns x of the Rectangle
        """
        return self.__x

    @property
    def y(self):
        """
        Returns y of the Rectangle
        """
        return self.__y

    @width.setter
    def width(self,value):
        """
        width setter
        """
        if type(value) != int:
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self,value):
        """
        height setter
        """
        if type(value) != int:
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @x.setter
    def x(self,value):
        """
        x setter
        """
        if type(value) != int:
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__x = value

    @y.setter
    def y(self,value):
        """
        y setter
        """
        if type(value) != int:
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__y = value
