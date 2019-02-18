# encode utf-8

import pandas as pd
import unittest

d = {'one': pd.Series([100., 200., 300.], index=['apple', 'ball', 'clock']),
     'two': pd.Series([111., 222., 333., 4444.], index=['apple', 'ball', 'cerill', 'dancy'])}
df = pd.DataFrame(d)


class BasicDateFrameOperations(unittest.TestCase):

    def test_show(self):
        print(df)

    def test_show_column(self):
        print(df['one'])

    def test_modify(self):
        df['three'] = df['one'] * df['two']
        print(df)

    def test_modify_02(self):
        df['flag'] = df['one'] > 250
        print(df)

    def test_pop(self):
        df['three'] = df['one'] * df['two']
        three = df.pop('three')
        print(three)
        print(df)

    def test_del(self):
        del df['two']
        print(df)

    def test_insert(self):
        df.insert(2, 'copy_of_one', df['one'])
        print(df)

    def test_insert_(self):
        df['one_upper_half'] = df['one'][:2]
        print(df)
