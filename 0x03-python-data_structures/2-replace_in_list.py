#!/usr/bin/python3

# Function that replaces an element at a specific position in a list
def replace_in_list(my_list, idx, element):

    # initiate condition as per requirements and return modified list
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)


# Stop script from CLI
if __name__ == "__main__":
    replace_in_list()
