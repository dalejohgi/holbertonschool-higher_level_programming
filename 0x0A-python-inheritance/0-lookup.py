#!/usr/bin/python3
"""
    Module 0-lookup
"""


def lookup(obj):
    """[Returns a list of atributtes of an object]

    Arguments:
        obj {Object of any type}

    Returns:
        [type] -- [List of objects atributtes]
    """
    return dir(obj)
