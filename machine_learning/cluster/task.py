# encoding utf-8

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from cluster.cleanning_data import data

features = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction',
            'max_wind_speed', 'relative_humidity']


def get_features():
    select_df = data[features]

    return StandardScaler().fit_transform(select_df)


def get_centers(scaler):
    kmeans = KMeans(n_clusters=12)
    model = kmeans.fit(scaler)

    return model.cluster_centers_


def pd_centers(featuresUsed, centers):
    colNames = list(featuresUsed)
    colNames.append('prediction')

    # Zip with a column called 'prediction' (index)
    Z = [np.append(A, index) for index, A in enumerate(centers)]

    # Convert to pandas data frame for plotting
    P = pd.DataFrame(Z, columns=colNames)
    P['prediction'] = P['prediction'].astype(int)
    return P


def parallel_plot(data):
    my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(data)))
    plt.figure(figsize=(15, 8)).gca().axes.set_ylim([-3, +3])
    parallel_coordinates(data, 'prediction', color=my_colors, marker='o')


if __name__ == '__main__':
    scaler = get_features()
    centers = get_centers(scaler)
    # print(type(centers))
    # print(centers.shape)
    # print(centers)
    pp = pd_centers(features, centers)
    print(pp.index)
    print(pp.columns)
    print(pp.head())
    parallel_plot(pp)
    # parallel_plot(pp[pp['relative_humidity'] < -0.5])
    # parallel_plot(pp[pp['air_temp'] > 0.5])
    # parallel_plot(pp[(pp['relative_humidity'] > 0.5) & (pp['air_temp'] < 0.5)])
    plt.show()
