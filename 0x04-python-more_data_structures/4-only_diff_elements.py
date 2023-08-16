#!/usr/bin/python3
def unique_elements(set_a, set_b):
    """
    returns a set of all elements present in only one set
    """
    combined_set = set_a | set_b
    return {element for element in combined_set if (element in set_a and element not in set_b) or
                                                  (element in set_b and element not in set_a)}
