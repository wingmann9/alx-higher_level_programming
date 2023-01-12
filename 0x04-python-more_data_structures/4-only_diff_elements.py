#!/usr/bin/python3

# Function show elements not common between two sets
def only_diff_elements(set_1, set_2):

    # Return elements different in  set_1 & set_2 - set()
    return (set_1 ^ set_2)
