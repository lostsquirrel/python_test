# encoding utf-8


import unittest
from matplotlib import pyplot as plt
from usa_co2_emission import get_usa_co2_emission, get_hist_data

stage = get_usa_co2_emission()
hist_data = get_hist_data(stage)


class USACO2EmissionPerCapita(unittest.TestCase):

    def test_show(self):
        print(stage.head())

    def test_change_over_time(self):
        # get the years
        years = stage['Year'].values
        # get the values
        co2 = stage['Value'].values

        # create
        plt.bar(years, co2)
        plt.show()

    def test_change_over_time_02(self):
        # switch to a line plot
        plt.plot(stage['Year'].values, stage['Value'].values)

        # Label the axes
        plt.xlabel('Year')
        plt.ylabel(stage['IndicatorName'].iloc[0])

        # label the figure
        plt.title('CO2 Emissions in USA')

        # to make more honest, start they y axis at 0
        plt.axis([1959, 2011, 0, 25])

        plt.show()

    def test_hist_show(self):
        print(len(hist_data))

    def test_hist(self):
        # the histogram of the data
        plt.hist(hist_data, 10, density=False, facecolor='green')

        plt.xlabel(stage['IndicatorName'].iloc[0])
        plt.ylabel('# of Years')
        plt.title('Histogram Example')

        plt.grid(True)

        plt.show()
