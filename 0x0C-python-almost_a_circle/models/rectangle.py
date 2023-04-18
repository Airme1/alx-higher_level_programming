#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, num):
            if type(num) is not int:
                raise TypeError("width must be an integer")
            elif num <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = num

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, num):
            if type(num) is not int:
                raise TypeError("height must be integer")
            elif num <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = num

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, num):
            if type(num) is not int:
                raise TypeError("x must be of type int")
            elif num < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, num):
            if type(num) is not int:
                raise TypeError("y must be of type int")
            elif num < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = num
