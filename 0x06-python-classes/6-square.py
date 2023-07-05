#!/usr/bin/python3
""" program to print square"""


class Square:
    """Square claas created"""
    def __init__(self, size=0, position=(0,0)):
        """Instantiation of class"""
        self.__size = size

    @property
    def size(self):
        """method to return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method to return area"""
        return (self.__size ** 2)

    def my_print(self):
        """method to print out square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()

    @property
    def position(self):
        return self.__position
