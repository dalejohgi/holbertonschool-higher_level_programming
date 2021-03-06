#!/usr/bin/python3
"""Module 10-square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class inherits from rectangle"""

    def __init__(self, size):
        """Initializer for square"""
        Rectangle.__init__(self, size, size)
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return(self.__size ** 2)
