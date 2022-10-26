import pandas as pd
import numpy as np

from data_prep.functions.utils import calc_weighted_average


def extract_top_movies(ratings_path: str, movies_path: str):
    ratings = pd.read_csv(ratings_path)
    movies = pd.read_csv(movies_path)

    movies['year'] = movies['title'].str.extract("(\d{4})")
    movies['title'] = movies['title'].str.replace("\s\([\d^)]*\)", '', regex=True)

    avg_ratings = ratings.groupby('movieId') \
                        .agg({'movieId': 'size', 'rating': 'mean'}) \
                        .rename(columns={'movieId': 'votes', 'avg_rating':''}) \
                        .reset_index()

    movies = movies.merge(avg_ratings, on='movieId')

    # calculate the average rating of all movies
    avg_pop = movies['rating'].mean()

    # consider only the movies with have more than 90% of the votes of the remainding movies
    min_votes = movies['votes'].quantile(0.9)
    top_movies = movies.copy().loc[movies['votes']>=min_votes]

    top_movies['score'] = top_movies.apply(lambda row : calc_weighted_average(row, min_votes=min_votes, avg_pop=avg_pop), axis=1)

    return top_movies

