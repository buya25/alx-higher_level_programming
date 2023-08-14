#!/usr/bin/python3

def print_matrix_integer(custom_matrix=[[]]):
    """
    Displays a matrix of integers to the standard output
    """
    for row in range(len(custom_matrix)):
        sub_matrix_len = len(custom_matrix[row])
        for col in range(sub_matrix_len):
            if col != sub_matrix_len - 1:
                ending_character = ' '
            else:
                ending_character = ''
            print("{:d}".format(custom_matrix[row][col]), end=ending_character)
        print("")
