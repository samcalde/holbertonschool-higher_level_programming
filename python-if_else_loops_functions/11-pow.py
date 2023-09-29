#!/usr/bin/python3
def pow(a, b):
    if (b == 0):
        return (1)
    result = 1
    if (b < 0):
        pwr = -b
    else:
        pwr = b
    for i in range(1, pwr+1):
        result = result * a
    if (b < 0):
        return (1/result)
    else:
        return (result)
