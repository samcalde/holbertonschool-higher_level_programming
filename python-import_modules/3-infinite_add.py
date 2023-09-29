#!/usr/bin/python3
import sys
argument_lenght = len(sys.argv)
arguments = sys.argv
total = 0

if (argument_lenght > 1):
    for i in range(1, (argument_lenght)):
        total = total + int(arguments[i])

print(total)
