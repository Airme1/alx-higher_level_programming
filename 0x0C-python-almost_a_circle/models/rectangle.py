#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """set default values"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return value of width"""
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
        """return value of height"""
        return self.__height

    @height.setter
    def height(self, num):
        """set height of rectangle"""
        if type(num) is not int:
            raise TypeError("height must be integer")
        elif num <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = num

    @property
    def x(self):
        """return value of x"""
        return self.__x

    @x.setter
    def x(self, num):
        """set value of y"""
        if type(num) is not int:
            raise TypeError("x must be of type int")
        elif num < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = num

    @property
    def y(self):
        """return value of y"""
        return self.__y

    @y.setter
    def y(self, num):
        """set value of y"""
        if type(num) is not int:
            raise TypeError("y must be of type int")
        elif num < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = num

    def area(self):
        """Return area of Rectangle"""
        return self.__height * self.__width

    def display(self):
        """display visual representation of rectangle"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """send user representation of string"""
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        if args != None:
            pos = 0
            for arg in args:
                if pos == 0:
                    self.id = arg
                elif pos == 1:
                   self.width = arg
                elif pos == 2:
                    self.height = arg
                elif pos == 3:
                    self.x = arg
                elif pos == 4:
                    self.y = arg
                pos += 1

        elif kwargs != 0:
            for k, v in kwargs.itmes():
                if k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
