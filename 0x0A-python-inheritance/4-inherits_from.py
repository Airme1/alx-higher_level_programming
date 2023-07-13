#!/usr/bin/python3
"""
Checks if object was inherited directly or 
indirectly from a class returns either True/False
"""


def inherits_from(obj, a_class):
    """Fxn return true is obj is instance of class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
