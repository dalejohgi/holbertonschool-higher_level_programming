#!/usr/bin/python3
"""Module 0-rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Function for build a rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the peri,eter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Builds the rectangle"""
        hash_rectangle = ""
        if self.width == 0 or self.height == 0:
            return hash_rectangle
        for i in range(self.height):
            hash_rectangle = hash_rectangle + ("#" * self.width)
            if i < self.height - 1:
                hash_rectangle += '\n'
        return hash_rectangle

    def __repr__(self):
        """return a string representation of the
           rectangle to be able to recreate a new instance"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter fot the width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter fot the height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
