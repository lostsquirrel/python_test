# encoding: utf-8
import unittest
from lec2 import *

class TestLec2(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(3), 9)

    def test_is_even(self):
        self.assertFalse(is_even(15))

    def test_least_1(self):
        self.assertEqual(least(15, 5, 11), 5)

    def test_least_2(self):
        self.assertEqual(least(15, 13, 11), 11)

    def test_int_square_root(self):
        self.assertEqual(int_square_root(16), 4)

    def test_divisor(self):
        self.assertEqual(divisor(10), [1, 2, 5])