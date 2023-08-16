#!/usr/bin/python3
def delete_key_from_dict(original_dict, delete_key=""):
    """
    deletes an element based on the key from a dictionary
    """
    if delete_key != "" and delete_key in original_dict:
        del original_dict[delete_key]
    return original_dict.copy()
