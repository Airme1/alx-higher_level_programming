#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    last_index = length-1
    for num in range(last_index, -1, -1):
        print("{}".format(my_list[num]))
