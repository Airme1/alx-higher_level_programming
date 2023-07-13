#!/usr/bin/python3
"""module to inherit from list class"""


class MyList(list):
    """this class inherits list"""
    def print_sorted(self):
        """method to sort list"""
        print(sorted(self))
