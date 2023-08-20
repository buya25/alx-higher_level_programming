#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is not None and isinstance(a_dictionary, dict):
        items = a_dictionary.items()
        to_delete = {key: val for (key, val) in items if value == val}
        for key in to_delete:
            del a_dictionary[key]
        return a_dictionary.copy()
