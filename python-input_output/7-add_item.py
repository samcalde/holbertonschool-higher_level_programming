#!/usr/bin/python3

"""
Adds all arguments to a Python list, and then save them to a file
"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args_len = len(sys.argv)
try:
    data_structure = load_from_json_file('add_item.json')
except:
    data_structure = []
for item in range(1, args_len):
    data_structure.append(sys.argv[item])
save_to_json_file(data_structure, 'add_item.json')
