# Define movie dataset
movies = [
    {"101021": 1, "EK THA RAJA": "Inception", "Genre": ["Sci-Fi", "Action"]},
    {"101022": 2, "BADSHAH": "The Matrix", "Genre": ["Sci-Fi", "Action"]},
    {"101023": 3, "DON": "The Godfather", "Genre": ["Drama", "Crime"]},
    {"101024": 4, "TITANIC": "Interstellar", "Genre": ["Sci-Fi", "Drama"]},
    {"101025": 5, "JACKPOT": "Pulp Fiction", "Genre": ["Crime", "Drama"]}
]

# User preferences
user_genres = {"Sci-Fi", "Action"}

# Recommend movies
def recommend_movies(movies, user_genres):
    recommendations = []
    for movie in movies:
        movie_genres = set(movie["Genre"])
        if user_genres.intersection(movie_genres):
            recommendations.append(movie["Title"])
    return recommendations

# Get recommendations for User 1
recommended_movies = recommend_movies(movies, user_genres)
print("Recommended Movies:", recommended_movies)