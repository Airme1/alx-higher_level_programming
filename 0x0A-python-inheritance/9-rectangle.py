#!/usr/bin/python3
"""Rectangle class to inherit from 7-base_geometry.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class to instantiate BaseGeometry"""
    def __init__(self, width, height):
        """function to filter and set width and height"""
        self.integer_validator("width",width)
        self.__width = width
        self.integer_validator("height",height)
        self.__height = height

    def area(self):
        """implementation of area in subclass method"""
        return self.__width * self.__height

    def __str__(self):
        """implement str method"""
        return '[Rectangle] {}/{}'.format(self.__width,self.__height)
