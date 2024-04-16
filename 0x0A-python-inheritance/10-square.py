#!/usr/bin/python3
"""Create a child-class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines Square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
