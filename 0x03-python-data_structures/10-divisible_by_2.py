#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    This finds all multiples of 2 in a list and returns
    a True or False list
    """
    list_len = len(my_list)
    if list_len == 0:
        return None

    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
