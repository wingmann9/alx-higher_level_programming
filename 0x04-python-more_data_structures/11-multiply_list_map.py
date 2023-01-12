#!/usr/bin/python3

# Function return values multiplied by a number without using loops
def multiply_list_map(my_list=[], number=0):

    # using map() & lambda() for multiplication
    return (list(map(lambda i: i*number, my_list)))
