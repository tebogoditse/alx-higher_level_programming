#!/usr/bin/python3
"""Function checks if obj is inherited instance of specified class"""


def inherits_from(obj, a_class):
    """checking..."""

    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False
