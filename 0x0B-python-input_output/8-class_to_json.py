#!/usr/bin/python3
"""
Contains the class_to_json function
"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure"""
    return obj.__dict__
