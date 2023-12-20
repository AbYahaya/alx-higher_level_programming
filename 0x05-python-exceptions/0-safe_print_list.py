#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    This functon prints the x element of a list.
    Returns falseif not an int
    """
    printedLen = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printedLen += 1
        except Exception:
            continue
    print()
    return printedLen
