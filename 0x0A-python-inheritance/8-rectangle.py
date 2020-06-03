#!/usr/bin/python3
"""Module 8-rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle"""

        BaseGeometry.integer_validator(self, width, height)
        self.__width = width
        self.__height = height
