#!/usr/bin/python3
"""THis module contains a class named rectangle
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
