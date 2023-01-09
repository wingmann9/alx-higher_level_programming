#!/usr/bin/python3

# Function finds multiples of 2 in a list
def divisible_by_2(my_list=[]):

    # using bool, make i mod 2 != 0 false instead
    new_list = [0 if i % 2 else 1 for i in my_list]
    return (list(map(bool, new_list)))


# Stop script from CLI
if __name__ == "__main__":
    divisible_by_2()
