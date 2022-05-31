#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10 if number > 0 else int(str(number)[-1]) * -1
    print("{}".format(last_digit))
    return last_digit
