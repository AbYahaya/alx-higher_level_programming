#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    This function prints all ints of a list, raises an Exception
    only when x is greater than lenght of the list
    """
    printedLen = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]),end="")
            printedLen += 1
        except (ValueError, TypeError):
            continue
    print()
    return printedLen

