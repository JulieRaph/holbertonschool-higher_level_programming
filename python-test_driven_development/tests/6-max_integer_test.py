#!/usr/bin/python3
"""
    Unittest for the function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1.5, 2.6, 3.7, 4.8]), 4.8)
        self.assertEqual(max_integer([1.5, 2.6, 3, 4.8]), 4.8)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)

    def test_none(self):
        self.assertEqual(max_integer(), None)

    def test_strings(self):
        self.assertEqual(max_integer(["School", "Day", "Friday", "Python"]), "School")

    def test_mixed(self):
        with self.assertRaises(TypeError):
            max_integer(["School", 2, 3, 4])

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()