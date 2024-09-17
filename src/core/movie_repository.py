from pymilvus import MilvusClient


class MovieRepository:

    next_id = 0

    def __init__(self) -> None:
        self.milvus_client = MilvusClient(uri="http://localhost:19530")
        self.collection_name = "movies"

    def get_next_id(self):
        self.next_id += 1
        return self.next_id

    def create_collection(self):
        if self.milvus_client.has_collection(self.collection_name):
            self.milvus_client.drop_collection(self.collection_name)

        self.milvus_client.create_collection(
            collection_name=self.collection_name,
            dimension=768,
            metric_type="IP",
            consistency_level="Strong",
        )

    def insert_movies(self, movies: list[dict]):
        data = [
            {
                "id": self.get_next_id(),
                "vector": movie["vector"],
                "plot": movie["plot"],
                "title": movie["title"],
            }
            for movie in movies
        ]

        self.milvus_client.insert(
            collection_name=self.collection_name, data=data
        )

    def find_movies(self, vector: list[float], limit: int):
        return self.milvus_client.search(
            collection_name=self.collection_name,
            data=[vector],
            limit=limit,
            search_params={"metric_type": "IP", "params": {}},
            output_fields=["id", "title", "plot", "vector"],
        )[0]
