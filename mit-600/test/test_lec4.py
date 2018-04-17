# encoding: utf-8
import unittest
from lec4 import *

class TestLec4(unittest.TestCase):

    def test_4leg_1heads(self):
        self.assertEqual(solve(4, 1), (1, 0))

    def test_2legs_1heads(self):
        self.assertEqual(solve(2, 1), (0, 1))

    def test_94legs_35heads(self):
        self.assertEqual(solve(94, 35), (12, 23))

    def test_3legs_2heads(self):
        self.assertEqual(solve(3, 2), (None, None))