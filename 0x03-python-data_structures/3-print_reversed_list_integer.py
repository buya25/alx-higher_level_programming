#!/usr/bin/python3

def print_reversed_list_integer(custom_list=[]):
    """
    Displays the reverse of a provided list of integers
    """
    if isinstance(custom_list, list):
        reversed_list = custom_list[:]
        reversed_list.reverse()
        for val in reversed_list:
            print("{:d}".format(val))
