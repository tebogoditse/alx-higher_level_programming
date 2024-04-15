#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """returns sorted list"""
    pass

    def print_sorted(self):
        print(sorted(list(self)))
