#!/usr/bin/python3
"""Replaces an element from a list"""


def replace_in_list(my_list, idx, element):
    if idx >= 0 or idx < len(my_list):
        my_list[idx] = element
    return my_list
