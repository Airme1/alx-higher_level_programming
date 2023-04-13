#!/usr/bin/python3
"""
Create Student class and attributes & retrieve dictionary
"""


class Student():
    def __init__(self, first_name, last_name, age):
        """initialize class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dictionary"""
        if attrs is not None:
            my_dict = {}
            for i in attrs:
                try:
                    my_dict[i] = self.__dict__[i]
                except Exception:
                    continue
            return my_dict
        else:
            return self.__dict__
