#!/usr/bin/python3

def delete_at(input_list=[], position=0):
    """
    Removes an element from a list at the specified position
    """
    list_length = len(input_list)
    if position >= list_length or position < 0:
        return input_list

    del input_list[position]
    return input_list
