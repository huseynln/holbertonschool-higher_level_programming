#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A class that defines a square by its size

    Attributes:
        __size: Private attribute representing the size of the square
    """

    def __init__(self, size):
        """Initialize a new Square instance

        Args:
            size: The size of the square (no type/value verification)
        """
        self.__size = size
