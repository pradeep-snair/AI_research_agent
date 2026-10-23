from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
ollama_base_url = os.getenv("OLLAMA_BASE_URL")
def create_embeddings(input_data:str):
    print(f"Input data is {input_data}")
    client = OpenAI(
        base_url=ollama_base_url,
        api_key="ollama"
    )
    response = client.embeddings.create(
        model="nomic-embed-text",
        input=input_data
    )
    embedding = response.data[0].embedding
    print(f"Length of Embedding is { len(embedding)} and type is {type(embedding)}")

if __name__ == "__main__":
    emb1 = create_embeddings("python is a coding lang")s