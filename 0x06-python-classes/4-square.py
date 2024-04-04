#!/usr/bin/python3
"""class Square."""


class Square:
    """empty class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property getter for size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter for size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= -1:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
