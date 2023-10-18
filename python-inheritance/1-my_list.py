#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
