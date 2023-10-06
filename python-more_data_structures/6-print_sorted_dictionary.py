#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(list(a_dictionary))
    for i in range(0, len(sorted_list)):
        print(f"{sorted_list[i]}: {a_dictionary[sorted_list[i]]}")
