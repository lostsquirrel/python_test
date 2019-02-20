# encode utf-8


from movie_data_analysis.data_clean import *


def test_split():
    print(movies.head())
    print()
    movie_genres = movies['genres'].str.split('|', expand=True)
    print(movie_genres[:10])
    print()
    movie_genres['isComedy'] = movies['genres'].str.contains('Comedy')
    print(movie_genres[:10])
    print()


def test_extract_year():
    movies['year'] = movies['title'].str.extract('.*\((.*)\).*', expand=True)
    print(movies.tail())
    print()


if __name__ == '__main__':
    test_split()
    test_extract_year()
