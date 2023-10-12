#!/usr/bin/python3

"""
Defines a class called rectangle
"""


class Rectangle:
    """
    Class called rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.increase_instances()

    @classmethod
    def increase_instances(cls):
        cls.number_of_instances += 1

    @classmethod
    def decrease_instances(cls):
        cls.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

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
        r = f"{str(self.print_symbol) * self.__width}\n" * (self.__height - 1)
        final_row = f"{str(self.print_symbol) * self.__width}"
        return (r + final_row)

    def __repr__(self):
        """
        String representation of the rectangle
        """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """
        Print the message when an instance of Rectangle is deleted
        """
        Rectangle.decrease_instances()
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_2.area() > rect_1.area()):
            return rect_2
        else:
            return rect_1
