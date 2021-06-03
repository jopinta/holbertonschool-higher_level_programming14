#!/usr/bin/python3
"""adds all arguments to a Python list"""

import json
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__ ("6-load_from_json_file").load_from_json_file

try:
    list = load_from_json_file(add_item.json)
except:
    list = []

for i in range(1, len(argv)):
    list.append(argv[i])
save_to_json_file(list, add_item.json)
