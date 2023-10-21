#!/usr/bin/python3

"""
returns a list of lists of integers representing the Pascal triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal triangle of n
    """
    if (n <= 0):
        return []
    pascal_list = []
    previous_list = [1]
    pascal_list.append(previous_list)
    list_length = 1
    for i in range(1, n):
        list_length += 1
        new_list = []
        for j in range(0, list_length):
            if (j == 0 or j == (list_length - 1)):
                new_list.append(1)
            else:
                new_list.append(previous_list[j - 1] + previous_list[j])
        previous_list = new_list
        pascal_list.append(new_list)
    return (pascal_list)
