#!/usr/bin/python3
"""A rectangle class with some string representation"""


class Rectangle:
    """Class definition for rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    """getter method for width"""
    def width(self):
        return self.__width

    @width.setter
    """width setter method"""
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
