#!/usr/bin/python3
import json 
"""
Function to return JSON representation of object
"""


def to_json_string(my_obj):
    """returns json rep of recieved object"""
    return json.dumps(my_obj)
