#!/usr/bin/python3

"""
A class MyList that inherits from list
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """
    def print_sorted(self):
        """
        prints the list, but sorted
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
