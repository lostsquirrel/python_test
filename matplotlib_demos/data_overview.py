# encoding utf-8

from data_load import data


def overview():
    print(data.shape)
    print(data.head(10))


def count_country_name():
    countries = data['CountryName'].unique().tolist()
    print(len(countries))


def count_country_code():
    # How many unique country codes are there ? (should be the same #)
    countryCodes = data['CountryCode'].unique().tolist()
    print(len(countryCodes))


def count_indicators():
    # How many unique indicators are there ? (should be the same #)
    indicators = data['IndicatorName'].unique().tolist()
    print(len(indicators))


def count_year():
    # How many years of data do we have ?
    years = data['Year'].unique().tolist()
    print(len(years))
    print(min(years), " to ", max(years))


if __name__ == '__main__':
    overview()
    count_country_name()
    count_country_code()
    count_indicators()
    count_year()
