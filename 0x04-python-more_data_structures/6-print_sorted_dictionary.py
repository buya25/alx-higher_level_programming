#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary with ordered keys. Keys are assumed to be strings.
    """
    [print("{}: {}".format(key, a_dictionary[key]))
        for key in sorted(a_dictionary)]
