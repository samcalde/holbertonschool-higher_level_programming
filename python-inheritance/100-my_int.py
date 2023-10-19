#!/usr/bin/python3

"""
Class that inherits from int and switches == and !=
"""
class MyInt(int):
    """
    Class that inherits from int
    """
    def __eq__(self, y):
        """
        Switch == for !=
        """
        return super().__ne__(y)

    def __ne__(self, y):
        """
        Switch != for ==
        """
        return super().__eq__(y)
