# encode utf-8

import pandas as pd

data_set_path = '/home/lisong/data-science/ml-20m'

movies = pd.read_csv('{}/movies.csv'.format(data_set_path), sep=',')
tags = pd.read_csv('{}/tags.csv'.format(data_set_path), sep=',')
# del tags['timestamp']
ratings = pd.read_csv('{}/ratings.csv'.format(data_set_path), sep=',', parse_dates=['timestamp'])
# del ratings['timestamp']

# For current analysis, we will remove timestamp (we will come back to it!)

