#!/usr/bin/python3

"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Makes 2 lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    lower_limit = 0
    higher_limit = 0
    i = 0
    for character in text:
        i += 1
        if character in (".", "?", ":"):
            higher_limit = i
            print(f"{text[lower_limit:higher_limit]}\n\n")
            lower_limit = i
    print(f"{text[lower_limit:]}")
