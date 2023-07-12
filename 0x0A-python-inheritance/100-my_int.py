#!/usr/bin/python3
"""Define a class called MyInt that inherits from int"""


class MyInt(int):
    """This is is the class MyInt that inherits from int"""

    def __eq__(self, other):
        """Overrides equality operator."""

        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides inequality operator."""

        return super().__eq__(other)
