#!/usr/bin/python3
"""
    0-add_integer module with add_integer function
"""


def add_integer(a, b=98):
    """
        Function that adds two integers

        Returns the result
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    elif type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return(int(a) + int(b))
