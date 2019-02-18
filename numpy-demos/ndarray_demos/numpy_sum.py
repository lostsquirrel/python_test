# encoding utf-8
import numpy as np
import unittest

ex1 = np.array([[11, 12], [21, 22]])


class NumpySum(unittest.TestCase):

    def test_sum_all(self):
        print(np.sum(ex1))  # add all members

    def test_sum_columns(self):
        print(np.sum(ex1, axis=0))  # columnwise sum

    def test_sum_rows(self):
        print(np.sum(ex1, axis=1))  # rowwise sum
