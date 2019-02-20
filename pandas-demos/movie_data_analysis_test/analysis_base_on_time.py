# encoding utf-8
from movie_data_analysis.read_data_set import read_movies, read_ratings, add_movies_year
import matplotlib.pyplot as plt

ratings = read_ratings()
movies = add_movies_year(read_movies())


def join_movie():
    average_rating = ratings[['movieId', 'rating']].groupby('movieId', as_index=False).mean()
    print(average_rating.tail())
    joined = movies.merge(average_rating, on='movieId', how='inner')
    print(joined.head())
    print(joined.columns)
    print()
    print(joined.corr())
    print()
    joinedx = joined[['year', 'rating']]
    print(joinedx)
    print()
    yearly_average = joinedx.groupby('year', as_index=False).mean()
    print(yearly_average[:10])

    yearly_average[-20:].plot(x='year', y='rating', figsize=(15, 10), grid=True)
    plt.show()


if __name__ == '__main__':
    join_movie()
