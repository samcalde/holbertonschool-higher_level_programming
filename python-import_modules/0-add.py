#!/usr/bin/python3
add = __import__("add_0").add

def add_funct():
    print("1 + 2 = ", add(1, 2))

if __name__ == "__main__":
    add_funct()
