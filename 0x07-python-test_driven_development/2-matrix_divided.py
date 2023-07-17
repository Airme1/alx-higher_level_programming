#!/usr/bin/python3
"""a module that divides a matrix"""


def matrix_divided(matrix, div):
    """function to divide each element of matrix by div"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    length = len(matrix[0])

    for sublist in matrix:
        if not isinstance(sublist, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            "of integers/floats")

        for val in sublist:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")

    for sublist in matrix:
        if length != len(sublist):
            raise TypeError("Each row of the matrix must have the"
                            "same size")

    return ([list(map(lambda x: round(x / div, 2), sublist))
            for sublist in matrix])
