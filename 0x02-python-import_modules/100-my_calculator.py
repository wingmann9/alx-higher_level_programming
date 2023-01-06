#!/usr/bin/python3
"""Stop script from CLI"""
if __name__ == "__main__":
    """Import functions from calculator_1.py file"""
    from calculator_1 import add, sub, mul, div
    import sys

    arg = len(sys.argv) - 1
    op = {"+": add, "-": sub, "*": mul, "/": div}
    if arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    """Operator sign must be present for function to execute"""
    if sys.argv[2] not in list(op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = op[sys.argv[2]](a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, result))
