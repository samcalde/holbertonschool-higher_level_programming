#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        try:
            if (size >= 0):
                self.__size = size
            elif (size < 0):
                raise ValueError('size must be >= 0')
        except TypeError:
            raise TypeError('size must be an integer')

    def area(self):
        self.area = self.__size * self.__size
        return (self.area)
