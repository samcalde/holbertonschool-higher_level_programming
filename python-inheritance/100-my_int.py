#!/usr/bin/python3

class MyInt(int):
    def __eq__(self, y):
        return super().__ne__(y)

    def __ne__(self, y):
        return super().__eq__(y)
