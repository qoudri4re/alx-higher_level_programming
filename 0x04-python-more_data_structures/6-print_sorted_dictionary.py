#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for dict_key in sorted(a_dictionary.keys()):
        print("{}: {}".format(value, a_dictionary[value]))
