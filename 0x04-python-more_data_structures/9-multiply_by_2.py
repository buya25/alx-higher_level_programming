#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Uses dictionary comprehension to multiply the value of every key-value
    pair in a dictionary by 2.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
