#!/usr/bin/python3

def no_c(input_str):
    """
    Removes all occurrences of 'c' and 'C' from a string
    """
    new_result_str = ""
    for char in input_str:
        if char != 'c' and char != 'C':
            new_result_str += char
    return new_result_str
