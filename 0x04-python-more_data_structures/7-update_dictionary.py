#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary and returns a new copy.
    The original dictionary is affected.
    """
    a_dictionary.update({key: value})
    return a_dictionary.copy()
