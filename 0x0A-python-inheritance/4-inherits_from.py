#!/usr/python3
"""
Checks if object was inherited directly or 
indirectly from a class returns either True/False
"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) or a_class != type(obj):
        return True
    else:
        return False
