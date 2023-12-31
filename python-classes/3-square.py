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
        try:
            if (size >= 0):
                self.__size = size
            elif (size < 0):
                raise ValueError('size must be >= 0')
        except TypeError:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Returns area of the square
        """
        self.area = self.__size * self.__size
        return (self.area)
