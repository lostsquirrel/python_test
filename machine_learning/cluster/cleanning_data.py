# encoding utf-8


from cluster.read_data import data

del data['rain_accumulation']
del data['rain_duration']

data = data.dropna()


def overview():
    print(data.shape)
    print(data.columns)
    print(data.head(3))


if __name__ == '__main__':
    overview()  # 158680
