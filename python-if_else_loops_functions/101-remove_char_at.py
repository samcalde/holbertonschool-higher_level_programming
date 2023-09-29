#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ""
    if ((n < 0) or (n > len(str))):
        return (str)
    else:
        for i in range(0, n):
            new_str += str[i]
        for i in range(n+1, len(str)):
            new_str += str[i]

    return (new_str)
