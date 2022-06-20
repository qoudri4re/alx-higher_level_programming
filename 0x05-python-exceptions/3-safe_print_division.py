#!/usr/bin/python3
def safe_print_division(a, b):
    res
    try:
        res = a / b
    except (ValueError,  TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {:d}".format(res))
    return res
