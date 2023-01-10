#!/usr/bin/python3
"""THis creates a class that can be serialized"""


class Student:
    """A class that can be encoded into json"""
    def __init__(self, first_name, last_name, age):
        """Initializes the attributes of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a serializable representation of the class"""
        if not attrs or not (isinstance(attrs, list) or
                             all(isinstance(am, str) for am in attrs)):
            return self.__dict__
        a = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                a[key] = value
        return a
