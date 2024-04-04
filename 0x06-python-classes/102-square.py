#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class """
    def __init__(self, size=0):
        """Initializes new instances of square."""
        self.__size = size

    def area(self):
        """Calculates the area of square."""
        return self.__size ** self.__size

    @property
    def size(self):
        """gets = the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, other):
        """Compares if square is < another"""
        return self.__size < other.__size

    def __le__(self, other):
        """Compares if square is <= another"""
        return self.__size <= other.__size

    def __eq__(self, other):
        """Compares if square is == another"""
        return self.__size == other.__size

    def __ne__(self, other):
        """Compares if square is != another"""
        return self.__size != other.__size

    def __gt__(self, other):
        """Compares if square is > another"""
        return self.__size > other.__size

    def __ge__(self, other):
        """Compares if square is >= another"""
        return self.__size >= other.__size
