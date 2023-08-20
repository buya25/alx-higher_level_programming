#!/usr/bin/python3

def mutiply_list_map(my_list=[], number=0):
    """
    Multiplies each element of a list by a given number using map and lambda.
    """
    return list(map(lambda x: x * number, my_list))
