#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except (ValueError,  TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {:f}".format(res))
    return res
