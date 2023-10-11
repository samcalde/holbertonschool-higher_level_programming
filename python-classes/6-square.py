#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    
    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position
    
    @size.setter
    def size(self, value):
        try:
            if (value >= 0):
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        except TypeError:
            raise TypeError('size must be an integer')
    
    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
                
    def area(self):
        return self.__size ** 2

    def my_print(self):
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
