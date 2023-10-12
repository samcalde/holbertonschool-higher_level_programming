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

    def area(self):
        """
        Returns area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns perimeter of rectangle
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Returns string to print the rectangle with the character #
        """
        if (self.__width == 0 or self.__height == 0):
            return ("")
        rows = (f"{'#' * self.__width}\n" * (self.__height - 1))
        final_row = f"{'#' * self.__width}"
        return (rows + final_row)
    
    def __repr__(self):
        """
        String representation of the rectangle
        """
        return (f"Rectangle({self.__width}, {self.__height})")
