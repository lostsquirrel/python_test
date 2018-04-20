# encoding: utf-8

import unittest
from lec5 import *


class TestLec5(unittest.TestCase):
    epsilon = 0.001
    tests = [(9, 3), (4, 2), (2, 1.414), (0.25, 0.5)]

    def test_square_root_bi(self):
        for pair in TestLec5.tests:
            self.assertTrue(abs(square_root_bi(pair[0], TestLec5.epsilon) - pair[1]) <= TestLec5.epsilon)

    def test_square_root_nr(self):
        for pair in TestLec5.tests:
            self.assertTrue(abs(square_root_nr(pair[0], TestLec5.epsilon) - pair[1]) <= TestLec5.epsilon)
