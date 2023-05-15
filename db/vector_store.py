import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction as Sbert_ef
import uuid

from config import VECTOR_STORE_PARAMS


client = chromadb.Client()


def get_collection():

    embedding_func = Sbert_ef(
        model_name=VECTOR_STORE_PARAMS['embedding_model'])

    # persist path is at .
    collection = client.get_or_create_collection(
        VECTOR_STORE_PARAMS['collection_name'], embedding_function=embedding_func)

    return collection


def uuid_gen():
    return uuid.uuid4().hex
