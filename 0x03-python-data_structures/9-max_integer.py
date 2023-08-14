#!/usr/bin/python3

def max_integer(custom_list=[]):
    """
    Finds the largest element in a list of integers
    """
    if len(custom_list) == 0:
        return None
    custom_list.sort()
    return custom_list[-1]
