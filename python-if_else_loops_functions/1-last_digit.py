#!/usr/bin/python3
import random

num = random.randint(-10000, 10000)

last_digit = num % 10

if (num < 0):
    last_digit = -num % 10
    last_digit = -last_digit
if ((last_digit == 0)):
    print(f"Last digit of {num} is {last_digit} and is 0")
elif (last_digit < 6):
    print(f"Last digit of {num} is {last_digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {num} is {last_digit} and is greater than 5")
