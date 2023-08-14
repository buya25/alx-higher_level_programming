#!/usr/bin/python3

def divisible_by_2(input_list=[]):
    """
    Identifies all elements in a list that are divisible by 2
    and returns a list containing True/False for each index
    """
    list_length = len(input_list)
    if list_length == 0:
        return None

    divisible_by_2_list = []
    for i in range(list_length):
        if input_list[i] % 2 == 0:
            divisible_by_2_list.append(True)
        else:
            divisible_by_2_list.append(False)
    return divisible_by_2_list
