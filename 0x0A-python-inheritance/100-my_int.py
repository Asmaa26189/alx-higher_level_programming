#!/usr/bin/python3
"""MyInt"""


class MyInt(int):
    """MyInt"""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
