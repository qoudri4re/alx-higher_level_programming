#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    try:
        tuple_a[0]
    except IndexError:
        tuple_a[0] = 0
    try:
        tuple_a[1]
    except IndexError:
        tuple_a[1] = 0
    try:
        tuple_b[0]
    except IndexError:
        tuple_b[0] = 0
    try:
        tuple_b[1]
    except IndexError:
        tuple_b[1] = 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
