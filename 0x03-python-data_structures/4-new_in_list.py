#!/usr/bin/python3

# Function replaces element without modifying the original list
def new_in_list(my_list, idx, element):

    # copy and make list immutable
    my_list = tuple(my_list)
    cp_list = list(my_list)

    # initiate condition and return both modified and original list
    if idx < 0 or idx > len(cp_list) - 1:
        return (cp_list)
    else:
        cp_list[idx] = element
        return (cp_list)
    return (list(my_list))


# Stop script from CLI
if __name__ == "__main__":
    new_in_list()
