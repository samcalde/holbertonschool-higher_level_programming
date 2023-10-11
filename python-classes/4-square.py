#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        try:
            if (value >= 0):
                self.__size = value
            elif (value < 0):
                raise ValueError('size must be >= 0')
        except TypeError:
            raise TypeError('size must be an integer')

    def area(self):
        return self.__size ** 2
