#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for item in list:
            print("{}".format(item), end = " ")
        print()
