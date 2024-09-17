from .embed import create_chat_completion, get_embedding, system, user
from .movie_repository import MovieRepository


class MovieWizard:

    def __init__(self):
        self.repository = MovieRepository()

    def find_movie_by_desc(self, movie_desc: str):
        movie_desc_vector = get_embedding(movie_desc)
        movie = self.repository.find_movies(movie_desc_vector, 1)[0]
        return movie

    def find_similar_movies(self, movie_vector: list[float]):
        similar_movies = self.repository.find_movies(movie_vector, 6)
        return similar_movies[1:]

    def recommend_movie(self, movie: dict, similar_movies: list[dict]):
        return create_chat_completion(
            [
                system(
                    """
You are a movie expert! I just have watched the movie described in the <movie>
tag. Please recommend me one of the recommended movies, that fits my movie
the best. Movies that are similar to the movie are in
<recommendationX> tags. Rephrase the recommended movie so that it fits my taste
and try to remove any spoilers. Also please keep the recommendation short.
Do not use any tags in your response, just answer plain text.
                """
                ),
                user(
                    f"""
<movie>
    {movie["entity"]["title"]}
    {movie["entity"]["plot"]}
</movie>
<recommendation1>
    {similar_movies[0]["entity"]["title"]}
    {similar_movies[0]["entity"]["plot"]}
</recommendation1>
<recommendation2>
    {similar_movies[1]["entity"]["title"]}
    {similar_movies[1]["entity"]["plot"]}
</recommendation2>
<recommendation3>
    {similar_movies[2]["entity"]["title"]}
    {similar_movies[2]["entity"]["plot"]}
</recommendation3>
"""
                ),
            ]
        )
