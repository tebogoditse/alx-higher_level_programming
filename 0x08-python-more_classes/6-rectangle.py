#!/usr/bin/python
"""Defines a class Rectangle"""


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        number_of_instances += 1

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

    def __str__(self):
        rectangle = []
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            return ((('#' * self.__width) + "\n") * self.__height)[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        number_of_instances -= 1
