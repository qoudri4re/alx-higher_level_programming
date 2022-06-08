#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = list(a_dictionary.keys())[0]
        for value in a_dictionary.values():
        if value > max:
            max = value
    return max
    else:
        return None
