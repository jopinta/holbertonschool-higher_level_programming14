#!/usr/bin/python3
"""function that creates an Object from JSON file"""

import json


def load_from_json_file(filename):
    """t need to manage exceptionsdon"""

    with open(filename, encoding='utf-8') as fp:
        return (json.load(fp.read()))
