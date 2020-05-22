#!/usr/bin/python3
"""
    Here goes de module docstring
"""


def say_my_name(first_name, last_name=""):
    """Here goes the fn docstring"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
