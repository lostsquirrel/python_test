# encoding utf-8

from data_load import data


def get_usa_co2_emission():
    # select CO2 emissions for the United States
    hist_indicator = 'CO2 emissions \(metric'
    hist_country = 'USA'

    mask1 = data['IndicatorName'].str.contains(hist_indicator)
    mask2 = data['CountryCode'].str.contains(hist_country)

    # stage is just those indicators matching the USA for country code and CO2 emissions over time.
    stage = data[mask1 & mask2]

    return stage


def get_hist_data(stage):
    # If you want to just include those within one standard deviation fo the mean, you could do the following
    # lower = stage['Value'].mean() - stage['Value'].std()
    # upper = stage['Value'].mean() + stage['Value'].std()
    # hist_data = [x for x in stage[:10000]['Value'] if x>lower and x<upper ]

    # Otherwise, let's look at all the data
    hist_data = stage['Value'].values
    return hist_data
