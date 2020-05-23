#!/usr/bin/python3
"""
    Module 4-print_square with print_square function
"""


def print_square(size):
    """Prints a square made of # of an specific size"""
    if type(size) is not int:
        raise TypeError('size must be an integer')
    else:
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            for i in range(size):
                print('#' * size, end="")
                print()
            if size == 0:
                print()
