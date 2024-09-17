from dotenv import load_dotenv
from .core.movie_repository import MovieRepository
from .core.embed import get_embedding

load_dotenv()

movie_desc = input("What did you just watch?\n")

desc_vector = get_embedding(movie_desc)

movie_repository = MovieRepository()

movie = movie_repository.find_movies(desc_vector, 1)[0]

score = movie["distance"]
movie = movie["entity"]

print(f"Movie: {movie['title']}")
print("\n")


similar_movies = movie_repository.find_movies(movie["vector"], 5)

print("Similar movies:")

for movie in similar_movies:
    movie = movie["entity"]
    print(f"Movie: {movie['title']}")
