#!/usr/bin/python3

for i in range(1, 27):
    if (i % 2 == 0):
        character = chr(123 - i -32)
    else:
        character = chr(123 - i)

    print("{}".format(character), end='')
