#!/usr/bin/python3
""" for JSON serialization of an object"""


def class_to_json(obj):
    """dictionary description"""
    return (obj.__dict__)
