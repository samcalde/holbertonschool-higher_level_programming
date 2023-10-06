#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for items in a_dictionary:
        new_dictionary[items] = (a_dictionary[items] * 2)
    return (new_dictionary)
