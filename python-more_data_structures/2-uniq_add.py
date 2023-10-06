#!/usr/bin/python3

def uniq_add(my_list=[]):
    used_int = []
    result = 0
    for i in range(0, len(my_list)):
        found = 'f'
        for j in range(0, len(used_int)):
            if (my_list[i] == used_int[j]):
                found = 't'
        if (found == 'f'):
            used_int.append(my_list[i])
            result = result + my_list[i]
    return (result)
