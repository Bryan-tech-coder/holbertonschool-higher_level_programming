#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a square using a single size value.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
