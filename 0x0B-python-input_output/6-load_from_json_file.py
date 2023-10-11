#!/usr/bin/python3
"""
function to create object from a json file
"""


import json


def load_from_json_file(filename):
    """create object from json file"""
    with open(filename, 'r') as jsn_file:
        return json.load(jsn_file)
