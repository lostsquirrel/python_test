# encode utf-8

import unittest
from movie_data_analysis.data_clean import *


class GroupByAggregate(unittest.TestCase):

    def test_rating_count(self):
        ratings_count = ratings[['movieId', 'rating']].groupby('rating').count()
        print(ratings_count)

    def test_movie_mean(self):
        average_rating = ratings[['movieId', 'rating']].groupby('movieId').mean()
        print(average_rating.head())

    def test_movice_count(self):
        movie_count = ratings[['movieId', 'rating']].groupby('movieId').count()
        print(movie_count.head())
        print(movie_count.tail())
