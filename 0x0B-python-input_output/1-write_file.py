#!/usr/bin/python3
"""
function to write a string to text file
and return a number of written characters
"""


def write_file(filename="", text=""):
    """method that writes data and returns lenght of text"""
    with open(filename, 'w', encoding="utf-8") as write_data:
        write_data.write(text)
        return len(text)
