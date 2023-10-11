#!/usr/bin/python3
"""
writing object to text file using json representation
"""


import json


def save_to_json_file(my_obj, filename):
    """writes into file from python args"""
    with open(filename, 'w') as obj_file:
        json.dump(my_obj, obj_file)
