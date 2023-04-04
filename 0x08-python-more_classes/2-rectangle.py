#!/usr/bin/python3
"""Getting Area and Perimeter of a Rectangle"""


class Rectangle:
    """Instatiation of rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    """setter method"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be and integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Using @decorator for height getter"""
    @property
    def height(self):
        return self.__height

    """setter method for height"""
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be and integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method that returns area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """method that returns the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)
