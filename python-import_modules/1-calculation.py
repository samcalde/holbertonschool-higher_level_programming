#!/usr/bin/python3
calculator = __import__("calculator_1")
a = 10
b = 5

print("{} + {} = {}".format(a, b, calculator.add(a, b)))
print("{} - {} = {}".format(a, b, calculator.sub(a, b)))
print("{} * {} = {}".format(a, b, calculator.mul(a, b)))
print("{} / {} = {}".format(a, b, calculator.div(a, b)))