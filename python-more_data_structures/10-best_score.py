#!/usr/bin/python3

def best_score(a_dictionary):
    if(a_dictionary == None):
        return(None)

    i = 1
    for item in a_dictionary:
        if (i == 1):
            biggest = item
            i += 1

        if (a_dictionary[item] > a_dictionary[biggest]):
            biggest = item
    return(biggest)
