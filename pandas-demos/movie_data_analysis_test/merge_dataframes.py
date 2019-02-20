# encode utf-8

import unittest
from movie_data_analysis.data_clean import *


class MergeDataFrames(unittest.TestCase):

    def test(self):
        print(tags.head())
        print()
        print(movies.head())
        print()
        t = movies.merge(tags, on='movieId', how='inner')
        print(t.head())
        print(t.columns)
