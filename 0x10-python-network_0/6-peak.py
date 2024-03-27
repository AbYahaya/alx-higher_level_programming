#!/bin/bash/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    The function to find a peak int
    """
    if len(list_of_integers) > 0:
        sort = list_of_integers.sort()
        return sort[-1]
    else:
        return None
