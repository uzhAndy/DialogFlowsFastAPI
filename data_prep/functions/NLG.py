import json


def create_response(title: str, release_year: str, genre: str, rating: float):
    if rating > 0:
        response = {
            "fulfillmentText": f'I recommend you watch the {genre} movie "{title}". It was the top movie of {release_year} with a rating of {round(rating, 2)}/5 stars.',
            "source": 'webhook'
        }
    else:
        response = {
            "fulfillmentText": f"I can't recommend a good {genre} movie from the year {release_year}, as there aren't any in the best 10% of movies of all time."
        }

    return response
