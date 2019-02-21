# encoding utf-8


from cluster.read_data import data


def overview():
    print(data.shape)
    print(data.columns)
    print(data.head(3))
    print(data.describe().transpose())
    print()


def rain_x_zero():
    print(data[data['rain_accumulation'] == 0].shape)
    print(data[data['rain_duration'] == 0].shape)


def has_null():
    print(data.isnull().shape)


if __name__ == '__main__':
    overview()  # 158725
    rain_x_zero()
    has_null()
