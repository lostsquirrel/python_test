# encoding: utf-8

from unittest import TestCase
from fractions import Fraction


class FractionsTest(TestCase):

    def test_simple(self):
        x = Fraction(1, 3)
        self.assertAlmostEqual(x, 0.33, 2)
        print(Fraction(6, 4))

    def test_math(self):
        self.assertEqual(Fraction(1, 3) * 2, Fraction(2, 3))

    def test_zero(self):
        self.assertRaises(ZeroDivisionError, Fraction, 5, 0)

