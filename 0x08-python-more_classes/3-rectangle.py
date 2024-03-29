#!/usr/bin/python3
"""A rectangle class with some string representation"""


class Rectangle:
    """Class definition for rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
         """width setter method"""
         if type(value) is not int:
             raise TypeError("width must be an integer")
         if value < 0:
             raise ValueError("width must be >= 0")
         else:
             self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """get area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """get perimeter of rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)
    
    def __str__(self):
        """print string representation of object"""
        st = ''
        for i in range(self.__height):
            for j in range(self.__width):
                st += '#'
            if i == self.__height -1:
                break
            st += '\n'
        return st
