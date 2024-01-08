#!/usr/bin/python3
# 7-base_geometry.py

"""BaseGeometry"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Vinteger_validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
