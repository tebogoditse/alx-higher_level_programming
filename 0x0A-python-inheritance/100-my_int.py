#!/usr/bin/python3
"""Class that inherits int"""


class MyInt(int):
    """inverts operators"""

    def __eq__(self, other):
        if self.real == other:
            return False
        return True

    def __ne__(self, other):
        if self.real != other:
            return False
        return True
