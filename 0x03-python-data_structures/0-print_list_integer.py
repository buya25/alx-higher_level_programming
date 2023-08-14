#!/usr/bin/python3

def print_list_integer(custom_list=[]):
    """
    Display a list of provided integers
    """
    for idx in range(len(custom_list)):
        print("{:d}".format(custom_list[idx]))
