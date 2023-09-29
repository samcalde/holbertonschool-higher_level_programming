#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import add, sub, mul, div

if (__name__ == "__main__"):
    argument_lenght = len(argv)
    arguments = argv

    if (argument_lenght != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif arguments[2] not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(arguments[1])
        b = int(arguments[3])
        if (arguments[2] == '+'):
            print("{} + {} = {}".format(a, b, add(a, b)))
        if (arguments[2] == '-'):
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if (arguments[2] == '*'):
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if (arguments[2] == '/'):
            print("{} / {} = {}".format(a, b, div(a, b)))
