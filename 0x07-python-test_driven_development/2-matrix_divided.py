#!/usr/bin/python3
"""
    Module 2-matrix_divided

    Contains the function matrix_divided which divide a matrix by an int
"""


def matrix_divided(matrix, div):
    """ Here goes the function doc string"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    rows_size = len(matrix[0])
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        for j in rows:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
        if rows_size != len(rows):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in [float, int]:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(j / div, 2) for j in rows] for rows in matrix]
