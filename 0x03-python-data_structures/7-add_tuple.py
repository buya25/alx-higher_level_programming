#!/usr/bin/python3

def add_tuple(tup_a=(), tup_b=()):
    """
    Combines the first two elements of two tuples element-wise and returns the result
    """
    len_a = len(tup_a)
    len_b = len(tup_b)
    result_tup = ()

    for i in range(2):
        val_a = 0 if i >= len_a else tup_a[i]
        val_b = 0 if i >= len_b else tup_b[i]

        if i == 0:
            result_tup = val_a + val_b
        else:
            result_tup = (result_tup, val_a + val_b)

    return result_tup
