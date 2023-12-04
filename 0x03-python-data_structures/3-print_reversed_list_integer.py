#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    prints the reverse of a given list
    """
    if type(my_list) is list:
        my_list.reverse()
        for itera in my_list:
            print("{:d}".format(itera))
