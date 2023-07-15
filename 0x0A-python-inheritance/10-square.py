#!/usr/bin/python3
"""Program to implement a square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class to create"""


    def __init__(self, size):
        """instantiate class"""
        self.integer_validator('size',size)
        super().__init__(size, size)
