#!/usr/bin/python3
"""In this module, we would get our introduction to getters and setters
for the first time"""


class Square:
    """This class contains three methonds:
        an init, a size, and area, then getter and setter"""
    def __init__(self, size=0, position=(0, 0)):
        """This initializes the string in a safe mode"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This is a getter function.
            It returns the value of size safely"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """This is the setter function. It prevents unwarranted modification
        of the size attribute by users"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """This is the getter fucntion to get the position safely"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """This gives us the position of the tuple to be printed"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This is the former area function.
        it gives the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """This prints out the square area onto the screen"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
