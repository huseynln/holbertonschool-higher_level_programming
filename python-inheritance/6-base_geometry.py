#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area method"""

    def area(self):
        """
        Calculates the area

        Raises:
            Exception: Always raises with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
