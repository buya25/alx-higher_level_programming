#!/usr/bin/python3

from add_0 import add as my_add_function

def main():
    a = 1
    b = 2
    result = my_add_function(a, b)
    print("{} + {} = {}".format(a, b, result))

if __name__ == "__main__":
    main()
