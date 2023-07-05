#!/usr/bin/python3
"""Class that defines rectangle"""


class Rectangle:
    """Rectangle class initiated"""
    def __init__(self, width=0, height=0):
        """instantiation of method"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the value of the (private) width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the (private) width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
