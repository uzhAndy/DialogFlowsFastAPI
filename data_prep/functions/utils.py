import pandas as pd
def calc_weighted_average(row: pd.Series, min_votes: int, avg_pop: float):
    """ Calculate the weighted average of a movie

    Args:
        row (pd.Series): the row which the weighted average is created for
        min_votes (int): minimum number of votes a movies has to receive to be considered
        avg_pop (float): average movie rating across the whole population
    min_votes: minumum number of 
    """
    votes = row['votes']
    avg_rt = row['rating']
    try:
        return (avg_rt * votes/(votes+min_votes)) + (avg_pop * min_votes/(votes + min_votes))
    except ZeroDivisionError:
        raise ZeroDivisionError