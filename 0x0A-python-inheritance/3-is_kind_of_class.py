#!/usr/bin/python3
"""Functions the return is obj is an instance of specified class"""


def is_kind_of_class(obj, a_class):
    """checking..."""

    if isinstance(obj, a_class):
        return True
    else:
        return False
