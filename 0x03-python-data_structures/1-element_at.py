#!/usr/bin/python3

def element_at(custom_list, position):
    """
    Retrieves an element from a list at the specified position
    Returns the element if valid, otherwise None
    """
    list_size = len(custom_list)
    if position >= list_size or position < 0:
        return None

    return custom_list[position]
