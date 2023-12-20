#!/usr/bin/python3

def safe_print_integer(value):
    """
    Funtion prints any integer but returns false if not an int
    """

    try:
        print("{:d}".format(value))
        return True
    except:
        return False
