# encode utf-8

import pandas as pd
import unittest

data = [{'alex': 1, 'joe': 2}, {'ema': 5, 'dora': 10, 'alice': 20}]


class CreateFromPythonDictionary(unittest.TestCase):

    def test_create(self):
        print(pd.DataFrame(data))

    def test_create_index(self):
        print(pd.DataFrame(data, index=['orange', 'red']))

    def test_create_columns(self):
        print(pd.DataFrame(data, columns=['joe', 'dora', 'alice']))
