#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    # return new dict() with 2 times the values of original dict()
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
