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
        self.integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self,value):
        """
        height setter
        """
        self.integer_validator("height", value)
        self.__height = value

    @x.setter
    def x(self,value):
        """
        x setter
        """
        self.integer_validator("x", value)
        self.__x = value

    @y.setter
    def y(self,value):
        """
        y setter
        """
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """
        Integer validator
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if (name in ("y", "x")) and value < 0:
            raise ValueError(f"{name} must be >= 0")
        if (name in ("width", "height")) and value <= 0:
            raise ValueError(f"{name} must be > 0")
    
    def area(self):
        """
        Returns area of the Rectangle instance
        """
        return (self.__width * self.__height)
    
    def display(self):
        for height in range(self.__height):
            for width in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        line1 = f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y}"
        line2 = f" - {self.__width}/{self.__height}"
        return (line1 + line2)
