#!/usr/bin/python3
"""Module 9-rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle"""

        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Claculates the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
