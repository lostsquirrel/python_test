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

    def test_conbine(self):
        avg_ratings = ratings.groupby('movieId', as_index=False).mean()
        del avg_ratings['userId']
        print(avg_ratings.head())
        print()
        box_office = movies.merge(avg_ratings, on='movieId', how='inner')
        print(box_office.tail())
        print()
        is_highly_rated = box_office['rating'] >= 4.0

        print(box_office[is_highly_rated][-5:])
        print()
        is_comedy = box_office['genres'].str.contains('Comedy')

        print(box_office[is_comedy][:5])
        print()
        print(box_office[is_comedy & is_highly_rated][-5:])
