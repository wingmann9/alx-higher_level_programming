#!/usr/bin/python3

# Function deletes element of a list at a specific point
def delete_at(my_list=[], idx=0):

    # conditional statement as per requirement
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    # iterate list to remove element at [idx]
    my_list[:] = [i for i in my_list if i != my_list[idx]]
    return my_list


# Stop script from CLI
if __name__ == "__main__":
    delete_at()
