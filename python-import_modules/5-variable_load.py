#!/usr/bin/python3

def var_load():
    variable_imported = __import__("variable_load_5")
    print(variable_imported.a)


if (__name__ == "__main__"):
    var_load()
