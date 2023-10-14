#!/usr/bin/python3

"""
Function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Function to divide elements
    """
    for rows in matrix:
        for element in rows:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0])
    for rows in matrix:
        if not (len(rows) == row_len):
            raise TypeError("row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for rows in matrix:
        new_list = []
        for element in rows:
            new_list.append("{:.2f}".format(element / div))
        new_matrix.append(new_list)
    return new_matrix
