#!/usr/bin/python3
"""
Check if object is the instance of a given class
"""


def is_kind_of_class(obj, a_class):
    """method to compare class and object"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
