# encoding utf-8

from classification.read_data import data


def remove_number(_data):
    del _data['number']
    return _data


def remove_null(_data):
    _data = _data.dropna()
    return _data


data = remove_null(remove_number(data))
