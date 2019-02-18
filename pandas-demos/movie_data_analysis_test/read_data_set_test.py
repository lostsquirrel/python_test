# encode utf-8

import unittest
from movie_data_analysis.read_data_set import *


def get_row(row):
    return tags.iloc[row]


class ReadDataset(unittest.TestCase):

    def test_show_movice(self):
        print(type(movies))
        print(movies.head(15))

    def test_show_rate_tag_head(self):
        print(ratings.head(), tags.head())


class SeriesTest(unittest.TestCase):

    def test_row_type(self):
        # Extract 0th row: notice that it is infact a Series

        row_0 = get_row(0)
        print(type(row_0))

    def test_show_row(self):
        print(get_row(0))

    def test_row_index(self):
        print(get_row(0).index)

    def test_row_data(self):
        print(get_row(0)['userId'])

    def test_in_row(self):
        print('rating' in get_row(0))

    def test_row_name(self):
        print(get_row(0).name)

    def test_rename_row(self):
        print(get_row(0).rename('first_row').name)


class DataFrameTest(unittest.TestCase):

    def test_head(self):
        print(tags.head())

    def test_index(self):
        print(tags.index)

    def test_columns(self):
        print(tags.columns)

    def test_iloc(self):
        print(tags.iloc[[0, 11, 2000]])
