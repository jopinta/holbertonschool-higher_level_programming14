#!/usr/bin/python3
"""inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """really true or false"""

    return (issubclass(obj, a_class))
