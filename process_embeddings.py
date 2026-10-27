from openai import OpenAI
from dotenv import load_dotenv
import os
import numpy as np
from litellm import embedding
from pathlib import Path
import tools
from tools_manager import execute_tool

load_dotenv()

# ollama_base_url = os.getenv("OLLAMA_BASE_URL")
data_folder_path = Path(os.getenv("DATA_FOLDER_PATH"))
ai_base_url=os.getenv("BASE_URL")
ai_api_key=os.getenv("API_KEY")
ai_embedding_model=os.getenv("EMBEDDING_MODEL")

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
    print(f"files are {files}")
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