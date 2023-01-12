#!/usr/bin/python3

# Function returns the weighted avg of all int in a tuple
def weight_average(my_list=[]):

    # Check that tuple is not empty
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    # iterate my_list and return the wavg
    avg = 0
    size = 0
    for tup in my_list:
        avg += (tup[0] * tup[1])
        size += tup[1]
    return (avg / size)
