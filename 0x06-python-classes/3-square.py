#!/usr/bin/python3
"""Empty class"""


class Square:
    """Square class wit a private attribute"""
    def __init__(self, size=0):
        """Initializes with a attribute size"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    def area(self):
        """Returns the area of a square"""
        return (int(self.__size) * int(self.__size))
