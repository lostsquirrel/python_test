# encode utf-8

import pandas as pd
import unittest

d = {'one': pd.Series([100., 200., 300.], index=['apple', 'ball', 'clock']),
     'two': pd.Series([111., 222., 333., 4444.], index=['apple', 'ball', 'cerill', 'dancy'])}
df = pd.DataFrame(d)


class CreateDataFrameFromDictionaryOfSeries(unittest.TestCase):

    def test_show(self):
        print(df)

    def test_index(self):
        print(df.index)

    def test_columns(self):
        print(df.columns)

    def test_create_index(self):
        print(pd.DataFrame(d, index=['dancy', 'ball', 'apple']))

    def test_create_index_columns(self):
        print(pd.DataFrame(d, index=['dancy', 'ball', 'apple'], columns=['two', 'five']))