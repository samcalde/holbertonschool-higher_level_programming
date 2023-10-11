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
        if type(size) is int:
            try:
                if (size >= 0):
                    self.__size = size
                elif (size < 0):
                    raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
