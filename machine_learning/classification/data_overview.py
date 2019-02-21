# encoding utf-8

from classification.read_data import data


def data_columns():
    print(data.columns)


def data_overview():
    print(data.head())


def data_count():
    print(data.shape[0])


def has_null_value():
    print(data[data.isnull().any(axis=1)].shape[0])


if __name__ == '__main__':
    data_columns()
    data_overview()
    data_count()  # 1095
    has_null_value()  # 31
