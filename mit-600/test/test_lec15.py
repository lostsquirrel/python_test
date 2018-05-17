# encoding: utf-8

import unittest
from lec15 import *


class TestLec15(unittest.TestCase):

    def test_add_points(self):
        self.assertEqual(add_points([1,2],  [3,1]), [4, 3])