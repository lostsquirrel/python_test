# encoding utf-8

from matplotlib import pyplot as plt
from data_load import data


def get_gdp():
    # select GDP Per capita emissions for the United States
    hist_indicator = 'GDP per capita \(constant 2005'
    hist_country = 'USA'

    mask1 = data['IndicatorName'].str.contains(hist_indicator)
    mask2 = data['CountryCode'].str.contains(hist_country)

    # stage is just those indicators matching the USA for country code and CO2 emissions over time.
    gdp_stage = data[mask1 & mask2]
    return gdp_stage


def gdp_plot():
    gdp_stage = get_gdp()
    # switch to a line plot
    plt.plot(gdp_stage['Year'].values, gdp_stage['Value'].values)

    # Label the axes
    plt.xlabel('Year')
    plt.ylabel(gdp_stage['IndicatorName'].iloc[0])

    # label the figure
    plt.title('GDP Per Capita USA')

    # to make more honest, start they y axis at 0
    # plt.axis([1959, 2011,0,25])

    plt.show()


if __name__ == '__main__':
    gdp_plot()
