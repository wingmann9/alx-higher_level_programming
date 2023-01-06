#!/usr/bin/python3
"""Stop module from command line import"""
if __name__ == "__main__":
    """import the function add(a, b) from add_0.py script"""
    import sys
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
"""Create the 0-import_add file"""
filename = "0-import_add.py"
myfile = open(filename, 'w')
myfile.write('__import__("0-add")\n')
myfile.close()

sys.exit()

