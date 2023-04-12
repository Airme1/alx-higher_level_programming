#!/usr/bin/python3
"""
Fxn to read a text file UTF8 and print to stdout
"""


def read_file(filename=""):
    """Fxn to receive and read file"""
    with open(filename, 'r', encoding="utf-8") as object_file:
        read_data = object_file.read()
        print(read_data)
