#!/usr/bin/python3
"""
Class BaseGeometry to raise Exceptions of
TypeError, ValueError
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """
        raise Exception
        """
        raise Exception("area is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
