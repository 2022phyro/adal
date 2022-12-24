#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_result(self):
        self.assertEqual(max_integer([1, 4, 5, 7, 3]), 7)
    def test_two_maximum_numbers(self):
        self.assertEqual(max_integer([1, 5, 2, 6, 7, 6, 7]), 7)
    def test_no_member_in_list(self):
        self.assertEqual(max_integer([]), None)