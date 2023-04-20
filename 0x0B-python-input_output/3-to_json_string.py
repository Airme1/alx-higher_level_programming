#!/usr/bin/python3 
"""
Function to return JSON representation of object
"""
import json


def to_json_string(my_obj):
    """returns json rep of recieved object"""
    return json.dumps(my_obj)
