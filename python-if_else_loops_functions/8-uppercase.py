#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ((ord(str[i]) > 96) and (ord(str[i]) < 123)):
            character = chr(ord(str[i])-32)
        else:
            character = str[i]
        print("{}".format(character), end='')
    print("")
