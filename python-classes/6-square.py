#!/usr/bin/python3

"""
Creating a class that represents a square
"""


class Square:
    """
    The class that represents a square with a size, taking errors into account
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """
        Returns size of square
        """
        return self.__size

    @property
    def position(self):
        """
        Returns position of square
        """
        return self.__position
    
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
            else:
                raise ValueError('size must be >= 0')
        except TypeError:
            raise TypeError('size must be an integer')
    
    @position.setter
    def position(self, value):
        """
        Defines the pos size

        Args:
            value (int): position of the square
        """
        if not (isinstance(value, tuple) and len(value) == 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
                
    def area(self):
        """
        Returns area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints area of square taking position into account
        """
        if (self.__size == 0):
            print("")
        else:
            for lines in range(0, self.position[1]):
                print("")
            for i in range(0, self.__size):
                for s in range(0, self.__position[1]):
                    print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print("")
