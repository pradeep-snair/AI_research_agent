from openai import OpenAI
import numpy as np
from litellm import embedding
import tools
from tools_manager import execute_tool

from config import (
    BASE_URL as ai_base_url,
    API_KEY as ai_api_key,
    EMBEDDING_MODEL as ai_embedding_model,
    DATA_FOLDER_PATH as data_folder_path,
)

def create_embeddings(input_data:str):
    """ function to create embedding for input data"""

    response = embedding(
        input=input_data,
        model=ai_embedding_model,
        api_base=ai_base_url,
        api_key=ai_api_key
    )
    return response.data[0]["embedding"]
    # Ollama code.
    # client = OpenAI(
        #     base_url=ollama_base_url,
        #     api_key="ollama"
        # )
        # response = client.embeddings.create(
        #     model="nomic-embed-text",
        #     input=input_data
        # )
        # response.data[0].embedding

def create_dataset_embeddings():
    """ function to create embedding for whole dataset in data dictionary"""
    files = [f for f in data_folder_path.iterdir() if f.is_file()]
    dataset_embeddings = {}
    for file in files:
        file_content = tools.read_file(file)
        dataset_embeddings = {file.name: create_embeddings(file_content)}
    return dataset_embeddings

def cosine_similiarity(vector1: list, vector2: list) -> float:
    v1 = np.asarray(vector1, dtype=float)
    v2 = np.asarray(vector2, dtype=float)
    denominator = np.linalg.norm(v1) * np.linalg.norm(v2)
    if denominator == 0:
        raise ValueError("Cannot calculate cosine similarity for a zero vector")

    return float(np.dot(v1,v2) / denominator)


if __name__ == "__main__":
    create_dataset_embeddings()