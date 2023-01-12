#!/usr/bin/python3

# Function print a dictionary sorted by keys
def print_sorted_dictionary(a_dictionary):

    # loop through dict() and print result
    [print("{}: {}".format(key, a_dictionary[key])) for key in sorted(a_dictionary)]
