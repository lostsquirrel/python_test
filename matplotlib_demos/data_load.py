# encoding utf-8

import pandas as pd

data_path = '/home/lisong/data-science/world-development-indicators'
data_file_name = 'Indicators.csv'

data = pd.read_csv('{}/{}'.format(data_path, data_file_name))
