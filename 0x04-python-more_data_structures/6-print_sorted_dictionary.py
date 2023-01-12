#!/usr/bin/python3

# Function prints a dict() in ordered keys
def print_sorted_dictionary(a_dictionary):

    # loop and print the items in dict() in alphabetic order
    [print(key,':', value) for key, value in sorted(a_dictionary.items())]
