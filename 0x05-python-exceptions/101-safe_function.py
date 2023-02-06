#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """
    Executes a function safely

    Args:
        fct: Function to execute
        args: Arguments to fct

    Returns:
        None - If exception occurs
        Otherwise - call to fct.
    """
    try:
        func_call = fct(*args)
        return (func_call)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
