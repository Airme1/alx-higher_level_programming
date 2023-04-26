#!/usr/bin/python3
"""Class to define square"""


class Square():
    def __init__(self, size=0):
        self.__size = size
        try:
            type(self.__size) == int
        except TypeError:
            print("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
