# encoding utf-8


from matplotlib import pyplot as plt
from data_load import data


def get_co2_2011():
    # select CO2 emissions for all countries in 2011
    hist_indicator = r'CO2 emissions \(metric'
    hist_year = 2011

    mask1 = data['IndicatorName'].str.contains(hist_indicator)
    mask2 = data['Year'].isin([hist_year])

    # apply our mask
    co2_2011 = data[mask1 & mask2]
    return co2_2011


def co2_emission_by_county():
    # let's plot a histogram of the emmissions per capita by country

    # subplots returns a touple with the figure, axis attributes.
    fig, ax = plt.subplots()

    ax.annotate("USA",
                xy=(18, 5), xycoords='data',
                xytext=(18, 30), textcoords='data',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3"),
                )
    stage = get_co2_2011()

    plt.hist(stage['Value'], 10, normed=False, facecolor='green')

    plt.xlabel(stage['IndicatorName'].iloc[0])
    plt.ylabel('# of Countries')
    plt.title('Histogram of CO2 Emissions Per Capita')

    # plt.axis([10, 22, 0, 14])
    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    co2_emission_by_county()
