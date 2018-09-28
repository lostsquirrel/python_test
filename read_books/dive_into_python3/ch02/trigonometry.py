# encoding: utf-8

from unittest import TestCase
import math

class TrigonometryTest(TestCase):

    def test_pi(self):
        print(math.pi)
        self.assertAlmostEqual(math.pi, 3.14159265, 8)

    def test_simple_sin(self):
        x = math.sin(math.pi / 2)
        print(x)
        self.assertEqual(x, 1)

    def test_simple_tan(self):
        x = math.tan(math.pi / 4)
        print(x)
        self.assertAlmostEqual(x, 1, 10)
