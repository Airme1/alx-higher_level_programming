#!/usr/bin/python3
"""
Adding a method to that replaces all attributes
of the Student instance
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

    def reload_from_json(self, json):
        """replace all attributes of Student instance"""
        for i in self.__dict__:
            try:
                self.__dict__[i] = json[i]
            except Exception:
                continue
