#!/usr/bin/python3

# Function to print a matrix of integers
def print_matrix_integer(matrix=[[]]):

    # iterate each element in the matrix
    for i in matrix:
        # convert and combine each element into a string
        j = (" ".join(map(str, i)))
        print("{:s}".format(j))


# Stop script from CLI
if __name__ == "__main__":
    print_matrix_integer()
