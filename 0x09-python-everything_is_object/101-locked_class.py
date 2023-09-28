#!/usr/bin/python3
# 101-locked_class.py
"""Defines a locked class"""


class LockedClass:
    """
    Prevent the dynamic creation of new instance attributes
    Except the attribute is "first_name"
    """
    
    __slots__ = ["first_name"]
