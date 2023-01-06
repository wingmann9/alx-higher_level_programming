#!/usr/bin/python3
"""Stop the function from CLI - command line import"""
if __name__ == "__main__":
    """Print the sum of a CL arguments"""
    import sys

    sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
