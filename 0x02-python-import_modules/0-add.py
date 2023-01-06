#!/usr/bin/env python3.8
"""Stop module from command line import"""
if __name__ == "__main__":
    """import the function add(a, b) from add_0.py script"""
    import sys
    import add_0

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add_0.add(a, b)))
    sys.exit()

