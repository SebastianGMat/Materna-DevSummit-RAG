import csv
from dotenv import load_dotenv
from .core.movie_repository import MovieRepository
from .core.embed import get_embedding

load_dotenv()


movie_repository = MovieRepository()
movie_repository.create_collection()


def process_chunk(chunk):
    movies = [
        {
            "title": movie[1],
            "plot": movie[7],
            "vector": get_embedding(movie[7]),
        }
        for movie in chunk
    ]

    movie_repository.insert_movies(movies)


with open("data/movies.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')

    # Skip the header
    header = next(reader)
    print("\n".join([f"{i}: {col}" for i, col in enumerate(header)]))

    # exit()

    CHUNK_SIZE = 10
    chunk = []
    count = 0

    for row in reader:
        chunk.append(row)
        if len(chunk) == CHUNK_SIZE:
            process_chunk(chunk)
            chunk = []
            count += CHUNK_SIZE

            print(f"Inserted {count} movies.")

    if chunk:
        process_chunk(chunk)
        count += len(chunk)

    print(f"Inserted {count} movies.")
