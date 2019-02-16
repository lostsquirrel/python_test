# encoding utf-8
import numpy as np
import unittest


s1 = np.array(['desk','chair','bulb'])
s2 = np.array(['lamp','bulb','chair'])

class SetOperations(unittest.TestCase):

    def test_show(self):
        print(s1, s2)

    def test_intersect1d(self):
        print(np.intersect1d(s1, s2))


    def test_union1d(self):
        print(np.union1d(s1, s2))

    def test_setdiff1d(self):
        print(np.setdiff1d(s1, s2))  # elements in s1 that are not in s2

    def test_in1d(self):
        print(np.in1d(s1, s2))  # which element of s1 is also in s2