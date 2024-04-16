#!/usr/bin/python3
"""Writes a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, attrVal):
    """adds new attribute"""

    if hasattr(obj, "__dict__"):
        setattr(obj, attr, attrVal)
    else:
        raise TypeError("Can't add new attribute")
