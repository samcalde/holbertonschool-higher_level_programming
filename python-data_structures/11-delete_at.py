#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if(idx < 0):
        return(my_list)
    elif(idx >= len(my_list)):
        return(my_list)
    else:
        for i in range(idx+1, len(my_list)):
            my_list[i - 1] = my_list[i]
        del my_list[i]
        return(my_list)
