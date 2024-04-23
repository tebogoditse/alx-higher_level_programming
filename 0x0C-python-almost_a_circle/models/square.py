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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates args"""
        if args is not None and len(args) != 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                    self.height = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        elif kwargs is not None and len(kwargs) != 0:
            for j in kwargs:
                if j == "id":
                    self.id = kwargs[j]
                elif j == "size":
                    self.width = kwargs[j]
                    self.height = kwargs[j]
                elif j == "x":
                    self.x = kwargs[j]
                elif j == "y":
                    self.y = kwargs[j]

    def to_dictionary(self):
        """retuns dictionary representation"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
