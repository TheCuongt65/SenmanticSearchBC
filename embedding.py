from milvus import Milvus, DataType
from typing import List
import numpy as np

class EmbeddingStorage:
    def __init__(self, host: str, port: str, collection_name: str):
        self.milvus = Milvus(host=host, port=port)
        self.collection_name = collection_name

    def create_collection(self, dimension: int):
        collection_param = {
            "collection_name": self.collection_name,
            "dimension": dimension,
            "index_file_size": 1024,  # optional
            "metric_type": DataType.FLOAT_VECTOR  # optional
        }
        status = self.milvus.create_collection(collection_param)

    def insert_vectors(self, vectors: List[np.array]):
        status, ids = self.milvus.insert(collection_name=self.collection_name, records=vectors)
        return ids

    def create_index(self):
        index_param = {
            'nlist': 2048
        }
        status = self.milvus.create_index(self.collection_name, index_param)

    def search_vectors(self, vectors: List[np.array], top_k: int):
        search_param = {
            "nprobe": 16
        }
        status, results = self.milvus.search(collection_name=self.collection_name, query_records=vectors, top_k=top_k, params=search_param)
        return results
