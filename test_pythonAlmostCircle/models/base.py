#!/usr/bin/python3
"""base"""
import json


class Base:
    """base."""
    __ini_Objects = 0

    def __init__(self, id=None):
        """init."""
        if id is not None:
            self.id = id
        else:
            Base.__ini_Objects += 1
            self.id = Base.__ini_Objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return (str(list_dictionaries))
