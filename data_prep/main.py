import json

from functions.data_import import extract_top_movies
from functions.data_service import get_movie_recommendation
from functions.NLG import create_response

if __name__ == '__main__':

    movies_list = 'data/movies.csv'
    ratings_list = 'data/ratings.csv'

    year = 1998
    genre = 'action'

    movies_df = extract_top_movies(movies_path=movies_list, ratings_path=ratings_list)
    movie = get_movie_recommendation(movies_df, year, genre)
    response = create_response(200, title=movie['title'], release_year=movie['year'], genres=movie['genres'], rating=movie['rating'])

    print(json.dumps(response[1], indent=2))