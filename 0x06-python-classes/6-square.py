#!/usr/bin/python3
"""class Square."""


class Square:
    """empty class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print("")
        for j in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                    print(" ",  end="")
            print("#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
