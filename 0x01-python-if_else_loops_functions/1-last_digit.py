#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = lastdigit = int(repr(number)[-1])
output = "Last digit of" + str(number) + "is" + str(last_digit)
if last_digit > 5:
    output += " and is greater than 5"
elif last_digit == 0:
    output += " and is 0"
elif last_digit < 5 and is not 0:
    output += " and is less than 6 and not 0"
