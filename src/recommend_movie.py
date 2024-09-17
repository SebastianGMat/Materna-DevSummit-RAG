from dotenv import load_dotenv
from .core.movie_wizard import MovieWizard

load_dotenv()


wizard = MovieWizard()

# movie_desc = "A young wizard and his friends defend their school"
# "against the dark lord."
movie_desc = input("What did you just watch?\n")


movie = wizard.find_movie_by_desc(movie_desc)

# print(movie)

print(f"It seems like you just watched the movie {movie["entity"]['title']}.")


similar_movies = wizard.find_similar_movies(movie["entity"]["vector"])

print("Here are some other movies, similar to yours:")

for similar_movie in similar_movies:
    print(f" - {similar_movie["entity"]['title']}")


print("Let me pick a recommendation for you...")

recommendation = wizard.recommend_movie(movie, similar_movies)

print(recommendation)
