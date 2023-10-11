#!/usr/bin/python3
"""
Program to return list of integers
representing the pascal triangle for n
"""

def pascal_triangle(n):
    my_list = []
    if n <= 0:
        return my_list
    else:
