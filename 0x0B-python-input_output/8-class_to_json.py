#!/usr/bin/python3
"""
returns dictionary description with simple data structure
"""


import json


def class_to_json(obj):
    """returns dictionary of object"""
    return obj.__dict__
