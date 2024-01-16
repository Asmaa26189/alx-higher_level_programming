#!/usr/bin/python3
"""base"""


class base:
    """base"""
    __ini_Objects = 0

    def __init__(self, id=None):
        """init"""
        if id not None:
            self.id = id
        else:
            __ini_Objects += 1
            self.id = __ini_Objects
