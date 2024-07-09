#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """find_peak"""
    max_i = None
    for i in list_of_integers:
        if max_i is None or max_i < i:
            max_i = i
    return max_i
