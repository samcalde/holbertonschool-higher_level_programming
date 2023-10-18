#!/usr/bin/python3

"""
Defines class Square that inherits from Rectangle
"""


class Square(__import__('9-rectangle').Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        if self.integer_validator("size", size):
            self.__size = size
            super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Returns rectangle description
        """
        return (f"[{__class__.__name__}] {self.__size}/{self.__size}")
