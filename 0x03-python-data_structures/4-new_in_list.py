#!/usr/bin/python3
"""Replaces an element from a list at a specific position"""


def new_in_list(my_list, idx, element):
    my_list_dup = my_list[:]
    if idx > -1 and idx <= len(my_list_dup) - 1:
        my_list_dup[idx] = element
    return my_list_dup
