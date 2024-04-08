#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.__height * self.__width
        return area

    def perimeter(self):
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return perimeter
        else:
            perimeter = 2 * (self.__width + self.__height)
            return perimeter
