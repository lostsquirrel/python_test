# encode utf-8

import unittest
from movie_data_analysis.data_clean import *


class DataClean(unittest.TestCase):

    def test_movies(self):
        print(movies.shape)
        print(movies.isnull().any())

    def test_rating(self):
        print(ratings.shape)
        print(ratings.isnull().any())

    def test_tags(self):
        print(tags.shape)
        print(tags.isnull().any())
