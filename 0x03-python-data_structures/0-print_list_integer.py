#!/usr/bin/python3

# Function that prints out the integers in a list
def print_list_integer(my_list=[]):

    # initiate a for loop to print each value in the list
    for i in my_list:
        print("{}".format(i))


# Stop the script from CLI
if __name__ == "__main__":
    print_list_integer()
