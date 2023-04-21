#!/usr/bin/python3
"""Square Program"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string representation"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'