#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in a_dictionary.keys():
        if key is value:
            del a_dictionary[key]
    return a_dictionary
