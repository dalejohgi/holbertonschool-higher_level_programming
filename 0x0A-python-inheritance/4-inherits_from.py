#!/usr/bin/python3
"""Module 4-inherits_from"""


def inherits_from(obj, a_class):
    """[Checks if an object inherits from a class]

    Arguments:
        obj {Object}
        a_class {Class}
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
