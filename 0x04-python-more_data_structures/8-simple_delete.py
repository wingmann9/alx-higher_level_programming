#!/usr/bin/python3

# Function deletes a key in a dictionary
def simple_delete(a_dictionary, key=""):

    # if key exist delete else return original list
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
