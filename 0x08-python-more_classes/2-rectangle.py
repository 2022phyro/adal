#!/usr/bin/python3
"""This module contains a class named rectangle
"""


class Rectangle:
    """This creates an empty class
    """

    def __init__(self, width=0, height=0):
        """This initializes the class

        Args:
            width (int, optional): the size. Defaults to 0.
            height (int, optional): the height. Defaults to 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

    def area(self):
        """Gives the area of the rectangle

        Returns:
            int: the area
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        """gives the perimeter of the rectangle

        Returns:
            int: the perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
