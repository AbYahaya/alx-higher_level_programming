#!/usr/bin/python3


def no_c(my_string):
    """
    removes characters 'c' and 'C' from a string
    """
    new_str = ""
    for letters in my_string:
        if letter not in "cC":
            new_str += letter
    return (new_str)
