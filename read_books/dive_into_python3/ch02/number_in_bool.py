# encoding: utf-8

from unittest import TestCase
from fractions import Fraction

class NumberInBool(TestCase):

    def test_ints(self):
        self.assertTrue(1)
        self.assertTrue(-1)
        self.assertFalse(0)

    def test_decimal(self):
        self.assertTrue(0.1)
        self.assertFalse(0.0)

    def test_fractions(self):
        self.assertFalse(Fraction(0, 2))
        self.assertTrue(Fraction(1, 2))