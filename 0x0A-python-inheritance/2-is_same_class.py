#!/usr/bin/python3
"""
Check if object is exactly an instance
of specified class
"""


def is_same_class(obj, a_class):
    """Comparing obj and a_class"""
    if type(obj) == type(a_class):
        return True
    else:
        return False
