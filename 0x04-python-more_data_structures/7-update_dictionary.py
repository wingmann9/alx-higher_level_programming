#!/usr/bin/python3

# Function create | replace key/value in a dictionary
def update_dictionary(a_dictionary, key, value):

    # condition to return original dict() if key already exist
    a_dictionary[key] = value
    return (a_dictionary)
