#!/usr/bin/python3
"""
    Here goes the module docstring
"""


def print_square(size):
    """Here goes the fn docstring"""
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
