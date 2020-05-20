#!/usr/bin/python3
"""Empty class"""


class Square:
    """Square class wit a private attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes with a attributes size and position"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if type(position) is not tuple \
           or type(position[0]) is not int \
           or type(position[1]) is not int \
           or len(position) != 2 \
           or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
                self.position = position

    def area(self):
        """Returns the area of a square"""
        return (int(self.__size) * int(self.__size))

    def my_print(self):
        """Print a square on the stdout"""
        if int(self.__size) == 0:
            print()
        else:
            if self.__position:
                print('\n' * self.__position[1], end="")
            for i in range(int(self.__size)):
                if self.__position:
                    print(' ' * self.__position[0], end="")
                print('#' * int(self.__size), end="")
                print()

    @property
    def size(self):
        """Returns the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    @property
    def position(self):
        """Returns the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute"""
        if type(value) is not tuple \
           or type(value[0]) is not int \
           or type(value[1]) is not int \
           or len(value) != 2 \
           or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
