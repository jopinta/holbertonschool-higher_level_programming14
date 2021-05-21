#!/usr/bin/python3
""" Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with
the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module
"""

def add_integer(a, b=98):

    for i in range(a, b):
    if i =! range(a, b)
    raise
    TypeError a must be an integer or b must be an integer
    if type(a) is float:
        a = int(a)
    if type(b) is float
        b = int(b)
    return (a + b)
