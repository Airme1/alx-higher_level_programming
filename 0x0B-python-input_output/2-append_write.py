#!/usr/bin/python3
"""
Function to append a string at end of text file
"""


def append_write(filename="", text=""):
    """append text and return length of text"""
    with open(filename, 'a', encoding="utf-8") as append_text:
        append_text.write(text)
        return len(text)
