#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(num):
        return (num * num)
    return [list(map(square, entry)) for entry in matrix]
