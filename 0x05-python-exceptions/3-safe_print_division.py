#!/usr/bin/python3

def safe_print_division(a, b):
    """
    This function divides two numbers and prints value under
    'Finally:'
    """
    res = 0
    try:
        res = a / b
        return res
    except Exception:
        res = None
        return res
    finally:
        print("Inside result: {}".format(res))
