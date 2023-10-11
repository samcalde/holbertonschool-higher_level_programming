#!/usr/bin/python3

"""
Creating a class that represents a square
"""


class Square:
    """
    The class that represents a square with a size, taking errors into account
    """
    def __init__(self, size=0):
        """
        Init for the square class oject

        Args:
            size (int): size of the square
        """
        self.size = size
    
    @property
    def size(self):
        """
        Returns size of square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Defines the square size

        Args:
            value (int): size of the square
        """
        try:
            if (value >= 0):
                self.__size = value
            elif (value < 0):
                raise ValueError('size must be >= 0')
        except TypeError:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Returns area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints area of square
        """
        if (self.__size == 0):
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print("")
