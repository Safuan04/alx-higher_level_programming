#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    for i in range(len(tuple_a)):
        if len(tuple_a) == 1:
            tuple_a = tuple_a[0], 0
        elif len(tuple_b) == 1:
            tuple_b = tuple_b[0], 0
        elif len(tuple_a) == 0:
            tuple_a = 0, 0
        elif len(tuple_b) == 0:
            tuple_b = 0, 0
        result.append(tuple_a[i] + tuple_b[i])
    return ((tuple_a[0] + tuple_b[0]),(tuple_a[1] + tuple_b[1]))
