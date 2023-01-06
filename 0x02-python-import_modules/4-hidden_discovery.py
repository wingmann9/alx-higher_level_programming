#!/usr/bin/python3
"""Stop the script from CLI"""
if __name__ == "__main__":
    """Print all names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    names = dir(hidden_4)
    for n in names:
        if n[:2] != "__":
            print(n)
