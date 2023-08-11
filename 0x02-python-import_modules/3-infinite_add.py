#!/usr/bin/python3
import sys

def calculate_sum(args):
    result = 0
    for arg in args:
        result += int(arg)
    return result

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    result = calculate_sum(sys.argv[1:])
    print("{:d}".format(result))
