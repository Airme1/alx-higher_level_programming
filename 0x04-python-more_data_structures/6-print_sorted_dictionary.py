#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.items())
    for k, v in a_dictionary:
        print('{}: {}'.format(k, v))
