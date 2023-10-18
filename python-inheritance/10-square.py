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
            super().__init__(size, size)
