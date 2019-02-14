# encoding utf-8
import numpy as np
import unittest


class FindUniqueElements(unittest.TestCase):

    def test(self):
        array = np.array([1, 2, 1, 4, 2, 1, 4, 2])

        print(np.unique(array))