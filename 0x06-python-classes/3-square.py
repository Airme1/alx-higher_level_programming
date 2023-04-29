#!/usr/bin/python3
class Square():
    """A class to find area of a square with a private instance attribute"""
    def __init__(self, size=0):
        """instantiation of class"""
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """Return area of square"""
        return self.__size * self.__size
