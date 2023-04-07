#!/usr/bin/python3
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([4, -3, 2, -1]), 4)
        self.assertEqual(max_integer([-1, 3, -2, 4]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([1.0, 2.5, 3.1, 4.6]), 4.6)
        self.assertEqual(max_integer([4.6, 3.1, 2.5, 1.0]), 4.6)
        self.assertEqual(max_integer([1.0, 3.1, 2.5, 4.6]), 4.6)

    def test_strings(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['c', 'b', 'a']), 'c')
        self.assertEqual(max_integer(['a', 'c', 'b']), 'c')

    def test_mixed_list(self):
        self.assertEqual(max_integer(['a', 2, -3, 4]), 'a')

if __name__ == '__main__':
    unittest.main()
