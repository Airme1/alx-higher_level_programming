#!/usr/bin/python3
"""
Raise exception: Area is not implemented
"""


class BaseGeometry:
    """class has just a method, no instantiation"""

    def area(self):
        """fxn to raise exception"""
        raise Exception("area() is not implemented")
