# encoding utf-8
import numpy as np
import unittest

# setup a random 2 x 4 matrix
arr = 10 * np.random.randn(2,5)

class BasicStatisticalOperations(unittest.TestCase):

    def test_show(self):
        print(arr)

    def test_mean(self):
        print(arr.mean())

    def test_mean_on_row(self):
        print(arr.mean(axis=1))

    def test_mean_on_column(self):
        print(arr.mean(axis=0))

    def test_sum(self):
        print(arr.sum())

    def test_median(self):
        print(np.median(arr, axis=1))