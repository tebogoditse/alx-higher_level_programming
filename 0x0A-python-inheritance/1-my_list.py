#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """returns sorted list"""

    def print_sorted(self):
        """prints the method"""
        return (sorted(self))
