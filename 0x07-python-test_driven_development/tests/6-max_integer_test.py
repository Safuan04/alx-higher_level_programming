#!/usr/bin/python3

"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 5, 7, 9, 4]), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -7, -9, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -5, 7, -9, 4]), 7)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 6, 7, 6, 7]), 7)

    def test_one_number(self):
        self.assertEqual(max_integer([7]), 7)

    def test_unsorted_numbers(self):
        self.assertEqual(max_integer([1, 5, 7, 9, 4]), 9)

    def test_sorted_numbers(self):
        self.assertEqual(max_integer([1, 4, 7, 8, 10]), 10)

    def test_large_numbers(self):
        self.assertEqual(max_integer([100, 500, 700, 900 ,400]), 900)


if __name__ == '__main__':
    unittest.main()
