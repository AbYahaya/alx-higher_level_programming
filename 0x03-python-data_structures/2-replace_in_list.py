#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    This will Replace an element in a list at a given index
    """
    if len(my_list) <= idx or idx < 0:
        return (my_list)

    my_list[idx] = element
    return (my_list)
