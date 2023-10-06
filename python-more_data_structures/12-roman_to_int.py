#!/usr/bin/python3

def roman_to_int(roman_string):
    if (roman_string is None or type(roman_string) != str):
        return (0)
    else:
        values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5}
        values['I'] = 1
        val_list = []
        strlen = len(roman_string)
        count = 0
        for i in range(strlen):
            current = roman_string[strlen - 1 - i]
            val_list.append(values[current])
        for j in range(0, len(val_list)):
            if ((j < len(val_list) - 1) and (val_list[j] > val_list[j + 1])):
                count += val_list[j]
                count -= 2 * val_list[j + 1]
            else:
                count += val_list[j]
        return (count)
