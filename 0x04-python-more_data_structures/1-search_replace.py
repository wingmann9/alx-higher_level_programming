#!/usr/bin/python3

# Function replace all occurrences of an element in a list
def search_replace(my_list, search, replace):

    # Create and return a new list that replace the element
    new_list = [replace if i == search else i for i in my_list]
    return (new_list)
