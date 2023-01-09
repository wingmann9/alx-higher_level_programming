#!/usr/bin/python3

# Function to remove character(s) from a string
def no_c(my_string):

    # initiate a new variable to form the modified string
    new_string = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(new_string))


# Stop the script from CLI
if __name__ == "__main__":
    no_c()
