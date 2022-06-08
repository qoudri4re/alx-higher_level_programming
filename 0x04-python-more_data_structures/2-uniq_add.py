#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    added_numbers = []
    for x in my_list:
        if x not in added_numbers:
            sum += int(x)
            added_numbers.append(x)
    return sum
