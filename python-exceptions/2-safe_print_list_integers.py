#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for item in range(0, x):
        try:
            print("{:d}".format(my_list[item]), end='')
            counter += 1
        except IndexError:
            print("Traceback (most recent call last):")
            return
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return (counter)
