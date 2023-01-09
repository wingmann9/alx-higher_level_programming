#!/usr/bin/python3

# Function that finds the max value in a list
def max_integer(my_list=[]):

    # initiate condition to check list and return None if [] else max integer
    return (None if my_list == [] else sorted(my_list)[-1])


# Stop script from CLI
if __name__ == "__main__":
    max_integer()
