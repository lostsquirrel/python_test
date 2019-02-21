# encoding utf-8

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from classification.clean_data import data


def binarize_relative_humidity_3pm():
    _data = data.copy()
    _data['high_humidity_label'] = (_data['relative_humidity_3pm'] > 24.99) * 1
    return _data


clean_data = binarize_relative_humidity_3pm()


def get_target(_data):
    y = _data[['high_humidity_label']].copy()
    return y


def get_features(_data):
    morning_features = ['air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am', 'avg_wind_speed_9am',
                        'max_wind_direction_9am', 'max_wind_speed_9am', 'rain_accumulation_9am',
                        'rain_duration_9am']
    x = _data[morning_features].copy()

    return x


def split_data_to_train_and_test(x, y):
    """
    x_train, x_test, y_train, y_test
    :param x:
    :param y:
    :return:
    """
    return train_test_split(x, y, test_size=0.33, random_state=324)


def train(x_train, y_train):
    humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
    humidity_classifier.fit(x_train, y_train)

    return humidity_classifier


def predict_on_test(humidity_classifier, x_test):
    predictions = humidity_classifier.predict(x_test)

    return predictions


def get_accuracy_score(predictions, y_test):
    return accuracy_score(y_true=y_test, y_pred=predictions)


def data_frame_overview(data_frame):
    print(data_frame.columns)
    print(data_frame.shape)
    print(data_frame.head())
    print()


if __name__ == '__main__':
    _data = binarize_relative_humidity_3pm()
    print(_data.columns)
    x = get_features(_data)
    print(x.columns)
    y = get_target(_data)
    print(y.columns)
    x_train, x_test, y_train, y_test = split_data_to_train_and_test(x, y)
    data_frame_overview(x_train)
    data_frame_overview(x_test)
    data_frame_overview(y_train)
    data_frame_overview(y_test)

    humidity_classifier = train(x_train, y_train)
    print(type(humidity_classifier))

    predictions = predict_on_test(humidity_classifier, x_test)
    print(predictions[:10])
    print(get_accuracy_score(predictions, y_test))
