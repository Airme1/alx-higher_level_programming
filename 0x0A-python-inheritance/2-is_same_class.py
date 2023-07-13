#!/usr/bin/python3
"""
Check if object is exactly an instance
of specified class
"""


def is_same_class(obj, a_class):
    """Comparing obj and a_class"""
    return type(obj) == a_class
