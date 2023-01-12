#!/usr/bin/python3

# Function delete keys with specific values in a dict()
def complex_delete(a_dictionary, value):

    # loop through dict.values() to delete the specofied key
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break
    return (a_dictionary)
