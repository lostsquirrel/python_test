# encoding utf-8


import pandas as pd
from movie_data_analysis.read_data_set import data_set_path

tags = pd.read_csv('{}/tags.csv'.format(data_set_path), sep=',')


def show_dtypes():
    print(tags.dtypes)


def parse_timestamp():
    print(tags.head(5))
    tags['parsed_time'] = pd.to_datetime(tags['timestamp'], unit='s')
    print(tags['parsed_time'].dtype)
    print(tags.head(2))


def select_by_time():
    greater_than_t = tags['parsed_time'] > '2015-02-01'

    selected_rows = tags[greater_than_t]

    print(tags.shape, selected_rows.shape)


def sort_by_time():
    print(tags.sort_values(by='parsed_time', ascending=True)[:10])


if __name__ == '__main__':
    show_dtypes()
    parse_timestamp()
    select_by_time()
    sort_by_time()
