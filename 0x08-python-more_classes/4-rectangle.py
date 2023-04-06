#!/usr/bin/python3
"""Evaluating expression for Retangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def print_rec(self):
        """print rectangle with #"""
        if self.width == 0 or self.__height == 0:
            return ""
        else:
            for n in range(self.__height):
                for m in range(self.__width):
                    print("#", end="")
                if n == self.__height - 1:
                    pass
                else:
                    print()

    def __str__(self):
        """print as string for user"""
        self.print_rec()
        return ""

    def __repr__(self):
        """print as represented on pc"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
