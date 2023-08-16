#!/usr/bin/python3
def dictionary_with_updated_key_value(original_dict, update_key, update_value):
    """
    updates a dictionary and returns a new copy
    original is affected
    """
    updated_dict = original_dict.copy()
    updated_dict[update_key] = update_value
    return updated_dict
