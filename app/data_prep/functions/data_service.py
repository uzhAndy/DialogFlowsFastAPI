import pandas as pd

def get_movie_recommendation(df: pd.DataFrame, year: int, genre:str):
    ignore_lower = '(?i)'
    
    movies = df.loc[(df['year']==str(year)) & (df['genres'].str.contains(f'{ignore_lower}{genre}'))]
    movies.reset_index()
    if not movies.empty:
        return movies.loc[movies['score'].idxmax()]
    else:
        return movies

def extract_filters(queryResult: dict):
    parameters: dict = queryResult.get('outputContexts')[0].get('parameters')
    return int(parameters.get('release_year')), parameters.get('genre')
