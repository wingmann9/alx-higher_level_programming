#!/usr/bin/python3

# Function sums up two tuples
def add_tuple(tuple_a=(), tuple_b=()):

    # condition to convert empty element in tuple to 0 and return sum
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return tuple(map(lambda a, b: a + b, tuple_a, tuple_b))
