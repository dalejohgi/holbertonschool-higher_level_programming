#!/usr/bin/python3
"""Module 2-is_same_calss"""


def is_same_class(obj, a_class):
    """[Evaluate classes]

    Arguments:
        obj {[Object]}
        a_class {[Class]}

    Returns:
        [Boolean] -- [True if the object belongs to the class, else False]
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
