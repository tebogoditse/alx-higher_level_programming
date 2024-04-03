#!/usr/bin/python3
"""class Square."""


class Square:
    """empty class"""
    def __init__(self, size=0):
        """initialize sqaure attributes"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size <= -1:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
