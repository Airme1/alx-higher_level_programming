#!/usr/bin/python3
"""Getting Area and Perimeter of a Rectangle"""


class Rectangle:
    """Instatiation of rectangle"""
    def __init__(self, width=0, height=0):
        """setting parameters"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method"""
        return self.__width
 
    @width.setter
    def width(self, value):
         """setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
 
    @property
    def height(self):
         """Using @decorator for height getter"""
        return self.__height

    @height.setter    
    def height(self, value):
         """setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
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
