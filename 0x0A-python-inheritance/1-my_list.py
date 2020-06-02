#!/usr/bin/python3
"""[summary]
"""


class MyList(list):
    """Class"""
    def __init__(self):
        """Initializer"""
        super().__init__()

    def print_sorted(self):
        """Function"""
        print(sorted(self))
