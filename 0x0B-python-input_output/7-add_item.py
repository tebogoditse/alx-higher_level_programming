#!/usr/bin/python3
"""Load, add, save"""


import json
import os.path
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list_json = []
if os.path.exists("add_item.json"):
    list_json = load_from_json_file("add_item.json")

for arg in range(1, len(sys.argv)):
    list_json.append(sys.argv[arg])

save_to_json_file(list_json, "add_item.json")
