#!/usr/bin/python3
def unique_sum(input_list=[]):
    """
    adds all unique elements of a list of ints together
    """
    return sum({element for element in input_list})
