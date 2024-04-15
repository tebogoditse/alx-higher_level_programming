#!/usr/bin/python3
"""Class definition"""


class MyList(list):
    """prints sorted list"""

    def print_sorted(self):
        print(sorted(list(self)))
