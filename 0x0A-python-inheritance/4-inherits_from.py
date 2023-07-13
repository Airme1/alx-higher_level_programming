#!/usr/python3
"""
Checks if object was inherited directly or 
indirectly from a class returns either True/False
"""


def inherits_from(obj, a_class):
    """Fxn return true is obj is instance of class"""
    return isinstance(obj, a_class)
