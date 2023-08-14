#!/usr/bin/python3

def replace_in_list(existing_list, position, new_value):
    """
    Modifies an element in a list at the specified position
    Returns the updated list
    """
    list_size = len(existing_list)
    if list_size <= position or position < 0:
        return existing_list

    existing_list[position] = new_value
    return existing_list
