# encoding utf-8
import numpy as np
import unittest

# create a 10 element array of randoms
unsorted = np.random.randn(10)
class Sorting(unittest.TestCase):

    def test_show(self):
        print(unsorted)

    def test_sort_on_copy(self):
        # create copy and sort
        sorted = np.array(unsorted)
        sorted.sort()

        print(sorted)
        print()
        print(unsorted)

    def test_sort_inplace(self):
        # inplace sorting
        print(unsorted)
        unsorted.sort()
        print()
        print(unsorted)