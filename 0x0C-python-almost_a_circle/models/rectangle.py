#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of a triangle"""
        area = self.__height * self.__width
        return area

    def display(self):
        """prints rectangle on stdout"""
        h = '\n' * self.y
        w = ' ' * self.x
        print_rectangle = h + (w + '#' * self.width + '\n') * self.height
        print(print_rectangle, end="")

    def __str__(self):
        """overiding __str__ method"""
        s = f"[{type(self).__name__}]"
        s1 = f"{s} ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return s1

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]
        elif kwargs is not None and len(kwargs) != 0:
            for j in kwargs:
                if j == 'id':
                    self.id = kwargs[j]
                elif j == 'width':
                    self.width = kwargs[j]
                elif j == 'height':
                    self.height = kwargs[j]
                elif j == 'x':
                    self.x = kwargs[j]
                elif j == 'y':
                    self.y = kwargs[j]
