#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        usr_list = list(eval(repr(self)))
        usr_list.sort()
        print(usr_list)

    """Exception handling fxn"""
    def excptn(self, num):
        if type(num) is not type(int):
            raise ValueError("Only integers permited in list")
        super().append(item)
