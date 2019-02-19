# encode utf-8

import unittest
import matplotlib.pyplot as plt
from movie_data_analysis.data_clean import *


class SliceOutColumns(unittest.TestCase):

    def test_one_column(self):
        print(tags['tag'].head())

    def test_more_columns(self):
        print(movies[['title', 'genres']].head())

    def test_x_row(self):
        print(ratings[-10:])

    def test_value_counts(self):
        tag_counts = tags['tag'].value_counts()
        print(tag_counts[-10:])
        tag_counts[:10].plot(kind='bar', figsize=(15, 10))
        plt.show()

    # def test_plot(self):
