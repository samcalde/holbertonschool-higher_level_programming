#!/usr/bin/python3

from add_0 import add

def add_funct():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(1, 2)))

if __name__ == "__main__":
    add_funct()
