#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if (my_list is None or len(my_list) == 0):
        return
    for i in range(0, len (my_list)):
        print("{:d}".format(len(my_list) - i))
