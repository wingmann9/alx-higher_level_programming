#!/usr/bin/python3

# Function that print in reverse order, elements in a list
def print_reversed_list_integer(my_list=[]):

    # reverse list and iterate each element
    for i in reversed(my_list):
        print("{:d}".format(i))


# Stop script from CLI
if __name__ == "__main__":
    print_reversed_list_integer()
