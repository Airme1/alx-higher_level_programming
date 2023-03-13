#!/usr/bin/python3

def max_integer(my_list=[]):
    comp = my_list[0]
    if my_list == []:
        return None
    else:
        for num in my_list:
            if num > comp:
                comp = num
    return comp
