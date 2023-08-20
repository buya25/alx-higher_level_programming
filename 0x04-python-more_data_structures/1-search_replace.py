#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of search with replace
    """
    return [ele if ele != search else replace for ele in my_list]
