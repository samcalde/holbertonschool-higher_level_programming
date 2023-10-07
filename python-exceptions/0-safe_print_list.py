#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0
    for item in range(0, x):
        try:
            print(my_list[item], end='')
            counter += 1
        except IndexError:
            break
    print("")
    return (counter)
