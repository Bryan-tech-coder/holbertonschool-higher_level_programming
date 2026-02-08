#!/usr/bin/env python3
"""
This module demonstrates duck typing using an abstract Shape class
and concrete Circle and Rectangle implementations.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Returns the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Returns the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape defined by its radius.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape defined by width and height.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
