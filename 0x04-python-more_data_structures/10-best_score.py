#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = list(a_dictionary.values())[0]
        for value in a_dictionary.values():
            if int(value) > int(max):
                max = value
        return max
    return None
