# encode utf-8

import pandas as pd

data_set_path = '/home/lisong/data-science/ml-20m'


# del tags['timestamp']

# del ratings['timestamp']

# For current analysis, we will remove timestamp (we will come back to it!)

def read_movies():
    movies = pd.read_csv('{}/movies.csv'.format(data_set_path), sep=',')
    return movies


def read_ratings():
    ratings = pd.read_csv('{}/ratings.csv'.format(data_set_path), sep=',', parse_dates=['timestamp'])
    return ratings


def read_tags():
    tags = pd.read_csv('{}/tags.csv'.format(data_set_path), sep=',')
    return tags


def add_movies_year(movies):
    movies['year'] = movies['title'].str.extract('.*\((.*)\).*', expand=True)
    return movies
