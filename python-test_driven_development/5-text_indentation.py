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
    j = 0
    for i in range(0, len(text)):
        if text[i] in (".", "?", ":"):
            if (text[j] == " "):
                while (text[j] == " "):
                    j += 1
            print(f"{text[j:i + 1]}\n")
            j = i + 1
    if (text[j] == " "):
        while (text[j] == " "):
            j += 1
    print(f"{text[j:]}", end="")
