#!/usr/bin/python3
"""function that validated whether obj is instance of specific class"""


def is_same_class(obj, a_class):
    """checking"""

    if type(obj) == a_class:
        return True
    else:
        return False
