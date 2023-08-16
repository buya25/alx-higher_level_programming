#!/usr/bin/python3
def print_ordered_dict(input_dict):
    """
    prints a dictionary by ordered keys. keys assumed to be strings
    """
    [print("{}: {}".format(key, input_dict[key])) for key in sorted(input_dict)]
