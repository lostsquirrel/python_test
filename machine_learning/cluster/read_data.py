# encoding utf-8

import pandas as pd

data_path = '/home/lisong/data-science/weather'
data_file_name = 'sample_minute_weather.csv'

data = pd.read_csv('{}/{}'.format(data_path, data_file_name))