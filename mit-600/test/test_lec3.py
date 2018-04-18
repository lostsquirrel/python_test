# encoding: utf-8
import unittest
from lec3 import *


class TestLec3(unittest.TestCase):

    def test_sum_digits(self):
        self.assertEqual(sum_digits(1952), 17)