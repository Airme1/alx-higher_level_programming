#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.sort(reverse = True)
    length = len(my_list) -1
    for num in range(0,length):
        print("{:d}".format(my_list[num]))
