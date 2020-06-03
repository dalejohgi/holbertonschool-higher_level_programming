#!/usr/bin/python3
def is_same_class(obj, a_class):
    """[Evaluate classes]

    Arguments:
        obj {[Object]}
        a_class {[Class]}

    Returns:
        [Boolean] -- [True if the object belongs to the class, else False]
    """
    return (type(obj) == a_class)