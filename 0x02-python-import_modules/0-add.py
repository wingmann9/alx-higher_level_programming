#!/usr/bin/python3

if __name__ == '__main__':

    import add_0
    """Import add() from add_0 file"""

    a = 1
    b = 2

    """Print the sum of a and b to stdout"""
    print('{} + {} = {}'.format(a, b, add_0.add(a,  b)))
