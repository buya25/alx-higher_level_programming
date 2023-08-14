#!/usr/bin/python3

def new_in_list(input_list, position, new_value):
    """
    Replaces an element in a list at a given position
    Creating a new list without modifying the original
    """
    list_length = len(input_list)
    if position >= list_length or position < 0:
        return input_list

    new_modified_list = input_list[:]
    new_modified_list[position] = new_value
    return new_modified_list
