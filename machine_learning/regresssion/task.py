# encoding utf-8

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from regresssion.cleanning_data import df

features = [
    'potential', 'crossing', 'finishing', 'heading_accuracy',
    'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
    'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
    'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
    'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
    'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
    'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
    'gk_reflexes']
target = ['overall_rating']


def get_features():
    return df[features]


def get_target():
    return df[target]


def liner_regression(x_train, y_train):
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    return regressor


def liner_regression_predict(regressor, x_test):
    return regressor.predict(x_test)


def cal_rmse(y_test, y_prediction):
    return sqrt(mean_squared_error(y_true=y_test, y_pred=y_prediction))


def decision_tree_regression(x_train, y_train):
    regressor = DecisionTreeRegressor(max_depth=20)
    regressor.fit(x_train, y_train)
    return regressor


def decision_tree_predict(regressor, x_test):
    return regressor.predict(x_test)


if __name__ == '__main__':
    x = get_features()
    # print(x.iloc[2])
    y = get_target()
    # print(y.head(3))
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.33, random_state=324)

    liner_regressor = liner_regression(X_train, Y_train)
    liner_predict = liner_regression_predict(liner_regressor, X_test)
    liner_rmse = cal_rmse(Y_test, liner_predict)
    print(liner_rmse)  # 2.8053030468552103

    dst_regressor = decision_tree_regression(X_train, Y_train)
    dst_predict = decision_tree_predict(dst_regressor, X_test)
    dst_rmse = cal_rmse(Y_test, dst_predict)
    print(dst_rmse)
