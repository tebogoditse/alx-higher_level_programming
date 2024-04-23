#!/usr/bin/python3
"""Squuare class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        name = type(self).__name__
        s = f"[{name}] ({self.id}) {self.x}/{self.y} - {self.width}"
        return s
