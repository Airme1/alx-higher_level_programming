#!/usr/bin/python3
import json
"""
writing object to text file using json representation
"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as obj_file:
        json.dump(my_obj, obj_file)
