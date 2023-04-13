#!/usr/bin/python3
import json
import sys
"""
Script thtat adds all argument to
a python list and saves to a file
"""


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"
try:
    obj = load_from_json_file(file)
except FileNotFoundError:
    with open(file, 'w') as json_file:
        obj = []
finally:
    obj += sys.argv[1:]
    save_to_json_file(obj, file)
