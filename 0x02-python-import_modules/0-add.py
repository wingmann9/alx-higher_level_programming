#!/usr/bin/python3
"""import add function from add-0 filw"""
import sys
from add_0 import add


def main():

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
    sys.exit()


"""stop script from CLI"""
if __name__ == "__main__":
    main()
