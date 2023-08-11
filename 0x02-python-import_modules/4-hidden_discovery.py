#!/usr/bin/python3
import sys
import hidden_4 as my_module

def print_non_hidden_attributes(module):
    for name in dir(module):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    print_non_hidden_attributes(my_module)
