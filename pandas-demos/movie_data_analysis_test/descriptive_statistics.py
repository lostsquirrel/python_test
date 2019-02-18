# encode utf-8

import unittest
from movie_data_analysis.read_data_set import ratings


class DescriptiveStatistics(unittest.TestCase):

    def test_describe_column(self):
        print('-------------------')
        print(ratings['rating'].describe())

    def test_describe_all(self):
        print('-------------------')
        print(ratings.describe())

    def test_mean(self):
        print('-------------------')
        print(ratings['rating'].mean())

    def test_mean_all(self):
        print('-------------------')
        print(ratings.mean())

    def test_filter(self):
        print('-------------------')
        filter_1 = ratings['rating'] > 5
        print(filter_1)
        print(filter_1.any())

        filter_2 = ratings['rating'] > 0
        print(filter_2.all())
