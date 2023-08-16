#!/usr/bin/python3
def multiply_values_by_2(input_dict):
    """
    using dictionary comprehension to multiply the value of every key: value
    pair in a dictionary
    """
    return {key: value * 2 for key, value in input_dict.items()}
