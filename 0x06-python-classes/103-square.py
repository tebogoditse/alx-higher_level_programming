#!/usr/bin/python3
"""Defines a class"""
import math
"""import math module"""


class MagicClass:
    """Class"""
    def __init__(self, radius=0):
        """Initialize instance"""
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Calculates the area"""
        return math.pi * (self.__radius * self.__radius)

    def circumference(self):
        """Calculates circ."""
        return 2 * math.pi * self.__radius
