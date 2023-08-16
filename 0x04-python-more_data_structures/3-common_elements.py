#!/usr/bin/python3
def find_common_elements(set_a, set_b):
    """
    returns a set of common elements from two sets
    """
    return {element for element in set_a if element in set_b}
