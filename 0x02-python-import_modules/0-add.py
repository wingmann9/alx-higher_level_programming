#!/usr/bin/python3

def main(a, b):
    """Print the sum of a and b to stdout"""
    print('{} + {} = {}'.format(a, b, add(a,  b)))


if __name__ == '__main__':
    from add_0 import add
    """Import add() from add_0 file"""

    a = 1
    b = 2
    main(a, b)
