#!/usr/bin/python3
"""Module 3-is_kind_off_class"""


def is_kind_of_class(obj, a_class):
    """[Checks if an object is an instance, or inherits from a class]

    Arguments:
        obj {Object}
        a_class {Class}
    """
    return (isinstance(obj, a_class))
