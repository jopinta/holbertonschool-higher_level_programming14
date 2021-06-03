#!/usr/bin/python3
"""writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """using a JSON representation:"""
    with open(filename, mode="w+", encoding='utf-8') as outfile:
        json.dump(my_obj, outfile)
