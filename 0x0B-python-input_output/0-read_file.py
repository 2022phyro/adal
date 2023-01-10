#!/usr/bin/python3
"""This file contains a function for reading"""


def read_file(filename=""):
    """This function reads from a text file and prints it to stdout"""
    with open(filename, 'r') as file_obj:
        print(file_obj.read())
