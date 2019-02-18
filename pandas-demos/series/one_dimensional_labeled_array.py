# encode utf-8

import pandas as pd
import unittest

ser = pd.Series([100, 'foo', 300, 'bar', 500], ['tom', 'bob', 'nancy', 'dan', 'eric'])


class OneDimensionalLabeledArray(unittest.TestCase):

    def test_show(self):
        print(ser)

    def test_index(self):
        print(ser.index)

    def test_loc(self):
        print(ser.loc[['nancy','bob']])

    def test_get_by_rank(self):
        print(ser[[4, 3, 1]])

    def test_iloc(self):
        print(ser.iloc[2])

    def test_in(self):
        print('bob' in ser)

    def test_change(self):
        print(ser * 2)

    def test_change_(self):
        print(ser[['nancy', 'eric']] ** 2)
