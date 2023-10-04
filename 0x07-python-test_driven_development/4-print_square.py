#!/usr/bin/python3
"""module that prints square"""


def print_square(size):
    """function to print square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == True:
        raise TypeError("size must be an integer")

    for height in range(size):
        for width in range(size):
            print('#',end='')
        print()
