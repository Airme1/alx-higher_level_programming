#!/usr/bin/python3
"""module to print name"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name = takes first name of user
        last_name = takse last name of user
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
