#!/usr/bin/python3

# Function that retrieve an element from a list
def element_at(my_list, idx):

    # initiate conditional statement and return thevalue
    return (None if idx < 0 or idx > (len(my_list) - 1) else my_list[idx])


# Stop script from CLI
if __name__ == "__main__":
    element_at()
