# packages
from data_prep.functions.data_import import extract_top_movies 
from data_prep.functions.data_service import extract_filters
from data_prep.functions.data_service import get_movie_recommendation
from data_prep.functions.NLG import create_response

# imports
from pydantic import BaseModel
from typing import Dict
from fastapi import FastAPI, status


class Request(BaseModel):
    responseId: str
    queryResult: Dict
    originalDetectIntentRequest: Dict
    session: str


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/click_me')
async def click_me():
    return {'message': 'Ich lieb dich, Angela!'}

@app.post('/movies')
async def get_movie(req_movie: Request):
    # try:
    body = req_movie.json()

    release_year, genre = extract_filters(req_movie.queryResult)

    print(f'Looking for:\t {release_year}\t--\t{genre}')

    movies_list = 'data/movies.csv'
    ratings_list = 'data/ratings.csv'

    movies_df = extract_top_movies(
        movies_path=movies_list, ratings_path=ratings_list)
    movie = get_movie_recommendation(movies_df, release_year, genre)
    if not movie.empty:
        response = create_response(title=movie['title'], release_year=movie['year'], genre=genre, rating=movie['rating'])
    else:
        response = create_response(title='No title', release_year=release_year, genre=genre, rating=0)
    return response