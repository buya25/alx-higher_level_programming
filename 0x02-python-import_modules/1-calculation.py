#!/usr/bin/python3
from calculator_1 import add as my_add, sub as my_sub, mul as my_mul, div as my_div

def print_operation_result(a, b, operation, result):
    print("{:d} {} {:d} = {:d}".format(a, operation, b, result))

if __name__ == "__main__":
    a = 10
    b = 5
    print_operation_result(a, b, "+", my_add(a, b))
    print_operation_result(a, b, "-", my_sub(a, b))
    print_operation_result(a, b, "*", my_mul(a, b))
    print_operation_result(a, b, "/", my_div(a, b))
