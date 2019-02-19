# encode utf-8

import unittest
from movie_data_analysis.data_clean import *


class FiltersSelectingRows(unittest.TestCase):

    def test_high_rated(self):
        is_highly_rated = ratings['rating'] >= 4.0

        print(ratings[is_highly_rated][30:50])

    def test_like(self):
        is_animation = movies['genres'].str.contains('Animation')

        print(movies[is_animation][5:15])
        print(movies[is_animation].head(15))
