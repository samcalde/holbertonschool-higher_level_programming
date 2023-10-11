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
        return self.__positio
    
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
        if (isinstance(value, tuple) and len(value) == 2):
            if(value[0] >= 0 and value[1] >= 0):
                self.__position = value
            else:
                raise TypeError('position must be a tuple of 2 positive integers')
        else:
            raise TypeError('position must be a tuple of 2 positive integers')
                
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print("")
