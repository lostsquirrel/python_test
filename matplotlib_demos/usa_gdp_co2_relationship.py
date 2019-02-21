# encoding utf-8

import numpy as np
import matplotlib.pyplot as plt
from usa_co2_emission import get_usa_co2_emission
from usa_gdp import get_gdp

stage = get_usa_co2_emission()
gdp_stage = get_gdp()
gdp_stage_trunc = gdp_stage[gdp_stage['Year'] < 2012]


def max_min():
    print("GDP Min Year = ", gdp_stage['Year'].min(), "max: ", gdp_stage['Year'].max())
    print("CO2 Min Year = ", stage['Year'].min(), "max: ", stage['Year'].max())


def confirm_data_size():
    print(len(gdp_stage_trunc))
    print(len(stage))


def correlation():
    print(np.corrcoef(gdp_stage_trunc['Value'], stage['Value']))


def plot():
    fig, axis = plt.subplots()
    # Grid lines, Xticks, Xlabel, Ylabel

    axis.yaxis.grid(True)
    axis.set_title('CO2 Emissions vs. GDP \(per capita\)', fontsize=10)
    axis.set_xlabel(gdp_stage_trunc['IndicatorName'].iloc[0], fontsize=10)
    axis.set_ylabel(stage['IndicatorName'].iloc[0], fontsize=10)

    X = gdp_stage_trunc['Value']
    Y = stage['Value']

    axis.scatter(X, Y)
    plt.show()


if __name__ == '__main__':
    max_min()
    confirm_data_size()
    correlation()
    plot()
