#!/usr/bin/python3
"""Evaluating expression for Retangle"""


class Rectangle:
    """class attributes stays here"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """instance attributes stay here"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
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
        """return area"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)


    def __str__(self):
        """print string representation of object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        st = ''
        for i in range(self.__height):
            for j in range(self.__width):
                st += str(self.print_symbol)
            if i == self.__height - 1:
                break
            st += '\n'
        return st

    def __repr__(self):
        """the object's python representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete instance of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method for comparing 2 instances"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method to create a square"""
        return cls(size, size)
