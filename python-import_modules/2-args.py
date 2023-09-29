#!/usr/bin/python3
import sys
argument_lenght = len(sys.argv)
arguments = sys.argv

if (argument_lenght <= 1):
	print("0 arguments.")
elif (argument_lenght == 2):
	print("{} argument:".format(argument_lenght - 1))
else:
	print("{} arguments:".format(argument_lenght - 1))

for i in range(1, (argument_lenght)):
	print("{}: {}".format(i, arguments[i]))